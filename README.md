
![Logo](docs/images/logo.png)

[![LICENSE](https://anaconda.org/brainpy/brainpy/badges/license.svg)](https://github.com/PKU-NIP-Lab/BrainPy)    [![Documentation](https://readthedocs.org/projects/brainpy/badge/?version=latest)](https://brainpy.readthedocs.io/en/latest/?badge=latest)     [![Conda](https://anaconda.org/brainpy/brainpy/badges/version.svg)](https://anaconda.org/brainpy/brainpy)    [![travis](https://travis-ci.org/PKU-NIP-Lab/BrainPy.svg?branch=master)](https://travis-ci.org/PKU-NIP-Lab/BrainPy)



**Note**: *BrainPy is a project under development. More features are coming soon. Contributions are welcome.*



## Why to use BrainPy

``BrainPy`` is a lightweight framework based on the latest Just-In-Time (JIT) compilers (especially [Numba](https://numba.pydata.org/)). The goal of ``BrainPy`` is to provide a unified simulation and analysis framework for neuronal dynamics with the feature of high flexibility and efficiency. BrainPy is flexible because it endows the users with the fully data/logic flow control. BrainPy is efficient because it supports JIT acceleration on CPUs (see the following comparison figure. In future, we will support JIT acceleration on GPUs).


![Speed of BrainPy](docs/images/speed.png)



## Installation

Install ``BrainPy`` using ``conda``:

    > conda install brainpy -c brainpy

Install ``BrainPy`` using ``pip``:

    > pip install git+https://github.com/PKU-NIP-Lab/BrainPy
    > # or
    > pip install git+https://git.openi.org.cn/OpenI/BrainPy
    > # Or
    > pip install -e git://github.com/PKU-NIP-Lab/BrainPy.git@V0.2.5


The following packages need to be installed to use ``BrainPy``:

- Python >= 3.7
- NumPy >= 1.13
- SymPy >= 1.2
- Numba >= 0.50.0
- Matplotlib >= 3.0


## Neurodynamics simulation


<table border="0">
    <tr>
        <td border="0" width="30%">
            <a href="examples/neurons/HH_model.py">
            <img src="docs/images/HH_neuron.png">
            </a>
        </td>
        <td border="0" valign="top">
            <h3><a href="examples/neurons/HH_model.py">HH Neuron Model</a></h3>
            <p>The Hodgkin–Huxley model, or conductance-based model,
            is a mathematical model that describes how action potentials
            in neurons are initiated and propagated. It is a set of nonlinear
            differential equations that approximates the electrical characteristics
            of excitable cells such as neurons and cardiac myocytes.</p>
        </td>
    </tr>
    <tr>
        <td border="0" width="30%">
            <a href="examples/synapses/AMPA.py">
            <img src="docs/images/AMPA_model.png">
            </a>
        </td>
        <td border="0" valign="top">
            <h3><a href="examples/synapses/AMPA.py">AMPA Synapse Model</a></h3>
            <p>AMPA synapse model.</p>
        </td>
    </tr>
    <tr>
        <td border="0" width="30%">
            <a href="examples/networks/gamma_oscillation.py">
            <img src="docs/images/gamma_oscillation.png">
            </a>
        </td>
        <td border="0" valign="top">
            <h3><a href="examples/networks/gamma_oscillation.py">Gamma Oscillation Model</a></h3>
            <p>Implementation of the paper: <i> Wang, Xiao-Jing, and György Buzsáki. “Gamma oscillation by
                  synaptic inhibition in a hippocampal interneuronal network
                  model.” Journal of neuroscience 16.20 (1996): 6402-6413. </i>
            </p>
        </td>
    </tr>
    <tr>
        <td border="0" width="30%">
            <a href="examples/networks/EI_balance_network.py">
            <img src="docs/images/EI_balance_net.png">
            </a>
        </td>
        <td border="0" valign="top">
            <h3><a href="examples/networks/EI_balance_network.py">E/I Balance Network</a></h3>
        </td>
    </tr>
    <tr>
        <td border="0" width="30%">
            <a href="examples/networks/CANN_1D.py">
            <img src="docs/images/CANN1d.png">
            </a>
        </td>
        <td border="0" valign="top">
            <h3><a href="examples/networks/CANN_1D.py">Continuous-attractor Network</a></h3>
            <p>Implementation of the paper: <i> Si Wu, Kosuke Hamaguchi, and Shun-ichi Amari. "Dynamics and
                    computation of continuous attractors." Neural
                    computation 20.4 (2008): 994-1025. </i>
            </p>
        </td>
    </tr>
</table>


More neuron examples please see [examples/neurons](https://github.com/PKU-NIP-Lab/BrainPy/tree/master/examples/neurons);

More synapse examples please see [examples/synapses](https://github.com/PKU-NIP-Lab/BrainPy/tree/master/examples/synapses);

More network examples please see [examples/networks](https://github.com/PKU-NIP-Lab/BrainPy/tree/master/examples/networks).




## Neurodynamics analysis



<table border="0">
    <tr>
        <td border="0" width="30%">
            <a href="examples/dynamics_analysis/NaK_model_analysis.py">
            <img src="docs/images/phase_plane_analysis1.png">
            </a>
        </td>
        <td border="0" valign="top">
            <h3><a href="examples/dynamics_analysis/NaK_model_analysis.py">Phase Plane Analysis</a></h3>
            <p>Phase plane analysis of the I<sub>Na,p+</sub>-I<sub>K</sub> model, where
            "input" is 50., and "Vn_half" is -45..</p>
        </td>
    </tr>
    <tr>
        <td border="0" width="30%">
            <a href="examples/dynamics_analysis/NaK_model_analysis.py">
            <img src="docs/images/NaK_model_codimension1.png">
            </a>
        </td>
        <td border="0" valign="top">
            <h3><a href="examples/dynamics_analysis/NaK_model_analysis.py">
                Codimension 1 Bifurcation Analysis (1)</a></h3>
            <p>Codimension 1 bifurcation analysis of the I<sub>Na,p+</sub>-I<sub>K</sub> model,
                in which "input" is varied in [0., 50.].</p>
        </td>
    </tr>
    <tr>
        <td border="0" width="30%">
            <a href="examples/dynamics_analysis/NaK_model_analysis.py">
            <img src="docs/images/NaK_model_codimension2.png">
            </a>
        </td>
        <td border="0" valign="top">
            <h3><a href="examples/dynamics_analysis/NaK_model_analysis.py">
                Codimension 2 Bifurcation Analysis (1)</a></h3>
            <p>Codimension 2 bifurcation analysis of a two-variable neuron model:
                the I<sub>Na,p+</sub>-I<sub>K</sub> model, in which "input" is varied
                in [0., 50.], and "Vn_half" is varied in [-50, -40].</p>
        </td>
    </tr>
    <tr>
        <td border="0" width="30%">
            <a href="examples/dynamics_analysis/FitzHugh_Nagumo_analysis.py">
            <img src="docs/images/FitzHugh_Nagumo_codimension1.png">
            </a>
        </td>
        <td border="0" valign="top">
            <h3><a href="examples/dynamics_analysis/FitzHugh_Nagumo_analysis.py">
                Codimension 1 Bifurcation Analysis (2)</a></h3>
            <p>Codimension 1 bifurcation analysis of FitzHugh Nagumo model, in which
                "a" is equal to 0.7, and "Iext" is varied in [0., 1.].</p>
        </td>
    </tr>
    <tr>
        <td border="0" width="30%">
            <a href="examples/dynamics_analysis/FitzHugh_Nagumo_analysis.py">
            <img src="docs/images/FitzHugh_Nagumo_codimension2.png">
            </a>
        </td>
        <td border="0" valign="top">
            <h3><a href="examples/dynamics_analysis/FitzHugh_Nagumo_analysis.py">
                Codimension 2 Bifurcation Analysis (2)</a></h3>
            <p>Codimension 2 bifurcation analysis of FitzHugh Nagumo model, in which "a"
               is varied in [0.5, 1.0], and "Iext" is varied in [0., 1.].</p>
        </td>
    </tr>
</table>


More examples please see [examples/dynamics_analysis](https://github.com/PKU-NIP-Lab/BrainPy/tree/master/examples/dynamics_analysis).






