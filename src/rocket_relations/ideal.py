import math
import numpy as np

def c_star(gamma, R, T0):
    """Calculate the theoretical characteristic velocity (c*) for an ideal rocket.

    Args:
        gamma: Ratio of specific heats (cp/cv).
        R: Specific gas constant [J/(kg·K)].
        T0: Stagnation (total) temperature [K].

    Returns:
        c_star: Theoretical characteristic velocity [m/s].

   """
    inputs = {
        "T0": T0,
        "gamma": gamma,
        "R": R,
    }
    
    for name, val in inputs.items():
        if not val.isnumeric:
            raise TypeError(f"{name} must be numeric or a NumPy array.")
    
    term1 = math.sqrt((1 / gamma) * ((2 / (gamma + 1)) ** ((gamma + 1) / (gamma - 1))))
    c_star = term1 * math.sqrt(R * T0)
    return c_star


def c_f(gamma, pe_p0, pa_p0, Ae_Astar):
    """
    Calculate the theoretical thrust coefficient (CF) for an ideal rocket.

    The thrust coefficient is defined as:
        CF = sqrt( (2*gamma^2 / (gamma - 1)) * ( (2 / (gamma + 1)) ** ((gamma + 1)/(gamma - 1)) ) *
                   [1 - (pe/p0) ** ((gamma - 1)/gamma)] ) + 
             (pe/p0 - pa/p0) * (Ae/A*)

    Args:
        gamma: Ratio of specific heats (cp/cv).
        pe_p0: Exit-to-stagnation pressure ratio (pe/p0).
        pa_p0: Ambient-to-stagnation pressure ratio (pa/p0).
        Ae_Astar: Nozzle area ratio (Ae/A*).

    Returns:
        CF: Theoretical thrust coefficient (dimensionless).


    """
    inputs = {
        "pe_p0": pe_p0,
        "area_ratio": Ae_Astar,
        "gamma": gamma,
        "pa_p0": pa_p0,
    }
    
    for name, val in inputs.items():
        if not val.isnumeric:
            raise TypeError(f"{name} must be numeric or a NumPy array.")
    
    term1 = math.sqrt(
        (2 * gamma**2 / (gamma - 1))
        * ((2 / (gamma + 1)) ** ((gamma + 1) / (gamma - 1)))
        * (1 - (pe_p0) ** ((gamma - 1) / gamma))
    )
    CF = term1 + (pe_p0 - pa_p0) * Ae_Astar
    return CF