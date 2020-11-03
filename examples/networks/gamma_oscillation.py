# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import brainpy as bp
import brainpy.numpy as np

bp.profile.set(backend='numba', device='cpu', dt=0.05, merge_steps=True,
               numerical_method='exponential')

# HH neuron model #
# --------------- #

spike_threshold = 0.

C = 1.0
gLeak = 0.1
ELeak = -65
gNa = 35.
ENa = 55.
gK = 9.
EK = -90.
phi = 5.0

HH_ST = bp.types.NeuState({'V': -55., 'h': 0., 'n': 0., 'sp': 0., 'inp': 0.})


@bp.integrate
def int_h(h, t, V):
    alpha = 0.07 * np.exp(-(V + 58) / 20)
    beta = 1 / (np.exp(-0.1 * (V + 28)) + 1)
    dhdt = alpha * (1 - h) - beta * h
    return phi * dhdt


@bp.integrate
def int_n(n, t, V):
    alpha = -0.01 * (V + 34) / (np.exp(-0.1 * (V + 34)) - 1)
    beta = 0.125 * np.exp(-(V + 44) / 80)
    dndt = alpha * (1 - n) - beta * n
    return phi * dndt


@bp.integrate
def int_V(V, t, h, n, Isyn):
    m_alpha = -0.1 * (V + 35) / (np.exp(-0.1 * (V + 35)) - 1)
    m_beta = 4 * np.exp(-(V + 60) / 18)
    m = m_alpha / (m_alpha + m_beta)
    INa = gNa * m ** 3 * h * (V - ENa)
    IK = gK * n ** 4 * (V - EK)
    IL = gLeak * (V - ELeak)
    dvdt = (- INa - IK - IL + Isyn) / C
    return dvdt


def update(ST, _t_):
    h = int_h(ST['h'], _t_, ST['V'])
    n = int_n(ST['n'], _t_, ST['V'])
    V = int_V(ST['V'], _t_, ST['h'], ST['n'], ST['inp'])
    sp = np.logical_and(ST['V'] < spike_threshold, V >= spike_threshold)
    ST['sp'] = sp
    ST['V'] = V
    ST['h'] = h
    ST['n'] = n
    ST['inp'] = 0.


HH = bp.NeuType('HH_neuron', requires={"ST": HH_ST}, steps=update)

# GABAa #
# ----- #

g_max = 0.1
E = -75.
alpha = 12.
beta = 0.1

requires = dict(
    ST=bp.types.SynState(['g', 's', 'pre_above_th']),
    pre=bp.types.NeuState(['V']),
    post=bp.types.NeuState(['V', 'inp']),
    pre2syn=bp.types.ListConn(),
    post2syn=bp.types.ListConn(),
)


@bp.integrate
def int_s(s, t, TT):
    return alpha * TT * (1 - s) - beta * s


def update(ST, _t_, pre, pre2syn):
    for pre_id, syn_ids in enumerate(pre2syn):
        ST['pre_above_th'][syn_ids] = pre['V'][pre_id] - spike_threshold
    T = 1 / (1 + np.exp(-ST['pre_above_th'] / 2))
    s = int_s(ST['s'], _t_, T)
    ST['s'] = s
    ST['g'] = g_max * s


def output(ST, post, post2syn):
    post_cond = np.zeros(len(post2syn), dtype=np.float_)
    for post_id, syn_ids in enumerate(post2syn):
        post_cond[post_id] = np.sum(ST['g'][syn_ids])
    post['inp'] -= post_cond * (post['V'] - E)


GABAa = bp.SynType('GABAa', requires=requires, steps=(update, output))

if __name__ == '__main__':
    num = 100
    v_init = -70. + np.random.random(num) * 20
    h_alpha = 0.07 * np.exp(-(v_init + 58) / 20)
    h_beta = 1 / (np.exp(-0.1 * (v_init + 28)) + 1)
    h_init = h_alpha / (h_alpha + h_beta)
    n_alpha = -0.01 * (v_init + 34) / (np.exp(-0.1 * (v_init + 34)) - 1)
    n_beta = 0.125 * np.exp(-(v_init + 44) / 80)
    n_init = n_alpha / (n_alpha + n_beta)

    neu = bp.NeuGroup(HH, geometry=num, monitors=['sp', 'V'])
    neu.ST['V'] = v_init
    neu.ST['h'] = h_init
    neu.ST['n'] = n_init

    syn = bp.SynConn(GABAa, pre_group=neu, post_group=neu,
                     conn=bp.connect.All2All(include_self=False),
                     monitors=['s', 'g'])
    syn.pars['g_max'] = 0.1 / num

    net = bp.Network(neu, syn)
    net.run(duration=500., inputs=[neu, 'ST.inp', 1.2], report=True, report_percent=0.2)

    ts = net.ts
    fig, gs = bp.visualize.get_figure(2, 1, 3, 12)

    fig.add_subplot(gs[0, 0])
    plt.plot(ts, neu.mon.V[:, 0])
    plt.ylabel('Membrane potential (N0)')
    plt.xlim(net.t_start - 0.1, net.t_end + 0.1)

    fig.add_subplot(gs[1, 0])
    index, time = bp.measure.raster_plot(neu.mon.sp, net.ts)
    plt.plot(time, index, '.')
    plt.xlim(net.t_start - 0.1, net.t_end + 0.1)
    plt.xlabel('Time (ms)')
    plt.ylabel('Raster plot')

    plt.show()