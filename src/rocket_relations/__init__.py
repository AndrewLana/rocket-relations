"""
c_star()    
Calculate the theoretical characteristic velocity (c*) for an ideal rocket.

    Args:
        gamma: Ratio of specific heats (cp/cv).
        R: Specific gas constant [J/(kg·K)].
        T0: Stagnation (total) temperature [K].

    Returns:
        c_star: Theoretical characteristic velocity [m/s].

c_f()
Calculate the theoretical thrust coefficient (CF) for an ideal rocket.

    Args:
        gamma: Ratio of specific heats (cp/cv).
        pe_p0: Exit-to-stagnation pressure ratio (pe/p0).
        pa_p0: Ambient-to-stagnation pressure ratio (pa/p0).
        Ae_Astar: Nozzle area ratio (Ae/A*).

    Returns:
        CF: Theoretical thrust coefficient (dimensionless).

"""
 
from .ideal import c_star, c_f
 
__all__ = ["c_star", "c_f"]