# -*- coding: utf-8 -*-
###############################################################################
# (c) Copyright 2016-2019 CERN for the benefit of the LHCb Collaboration      #
#                                                                             #
# This software is distributed under the terms of the GNU General Public      #
# Licence version 3 (GPL Version 3), copied verbatim in the file "COPYING".   #
#                                                                             #
# In applying this licence, CERN does not waive the privileges and immunities #
# granted to it by virtue of its status as an Intergovernmental Organization  #
# or submit itself to any jurisdiction.                                       #
###############################################################################


def get_g_info(g_flag):
    g_dict = {}
    g_dict[0] = { "meaning" : "(illegal value)", type : "error"} 
    g_dict[1] = { "meaning" : "events containing a b quark, extracted from a minimum bias sample", type : "info"} 
    g_dict[2] = { "meaning" : "events containing a c quark, extracted from a mimimum bias sample", type : "info"} 
    g_dict[3] = { "meaning" : "events without b and c quark, extracted from a minimum bias sample", type : "info"} 
    g_dict[4] = { "meaning" : "non-flavour physics with special generator settings", type : "info"} 
    g_dict[5] = { "meaning" : "particle guns", type : "info"} 
    g_dict[6] = { "meaning" : "machine induced background (MIB) events", type : "info"} 
    g_dict[7] = { "meaning" : "(reserve)", type : "error"} 
    g_dict[8] = { "meaning" : "(reserve)", type : "error"} 
    g_dict[9] = { "meaning" : "real data", type : "info"}
    return g_dict[g_flag]

def get_s_info_dict(g_flag):
    s_dict = {}
    if g_flag == 1:
        s_dict[0] = { "meaning" : "a bhadron, amongst a list of more than one specified species, is required", "type" : "info"}
        s_dict[1] = { "meaning" : "a $B^0$ is required", "type" : "info"}
        s_dict[2] = { "meaning" : "a $B^+$ is required", "type" : "info"}
        s_dict[3] = { "meaning" : "a $B_s^0$ is required", "type" : "info"}
        s_dict[4] = { "meaning" : "a $B_c^+$ is required", "type" : "info"}
        s_dict[5] = { "meaning" : "a $\Lambda_b$ is required", "type" : "info"}
        s_dict[6] = { "meaning" : "a specific b-baryon, other than $\Lambda_b$, is required the extra flag specifies the type of baryon", "type" : "info"}
        s_dict[7] = { "meaning" : "a b-hadron resonance is required, the extra flag specifies the type of resonance", "type" : "info"}
        s_dict[8] = { "meaning" : "a bb̄-meson  is required, the extra flag specifies the type of resonance", "type" : "info"}
        s_dict[9] = { "meaning" : "two or more b-hadrons, amongst a list of specified combinations, are required", "type" : "info"}

    elif g_flag == 2:
        s_dict[0] = { "meaning" : "a c-hadron, amongst a list of more than one specified species, is required", "type" : "info"}
        s_dict[1] = { "meaning" : "a $D^−$ is required", "type" : "info"}
        s_dict[2] = { "meaning" : "a $D^0$ is required", "type" : "info"}
        s_dict[3] = { "meaning" : "a $D_s^-$ is required", "type" : "info"}
        s_dict[4] = { "meaning" : "a $J/\psi$ is required", "type" : "info"}
        s_dict[5] = { "meaning" : "a $\Lambda_c$ is required", "type" : "info"}
        s_dict[6] = { "meaning" : "a specific c-baryon, other than $\Lambda_c$, is required the extra flag specifies the type of baryon, see Table 12 and Table 13", "type" : "info"}
        s_dict[7] = { "meaning" : "a c-hadron resonance is required, the extra flag specifies the type of resonance", "type" : "info"}
        s_dict[8] = { "meaning" : "a (cc̄-meson other than $J/\psi$) is required, the extra flag specifies the type of resonance", "type" : "info"}
        s_dict[9] = { "meaning" : "two or more c-hadrons, amongst a list of specified combinations, are required", "type" : "info"}

    elif g_flag == 3:
        s_dict[0] = { "meaning" : "no requirement", "type" : "info"}
        s_dict[1] = { "meaning" : "a $\\tau^+$ + or $\\tau^-$ is required. (See LHCb Note 2009-001 for more details)", "type" : "info"}
        s_dict[2] = { "meaning" : "a $\Sigma^+$ or $\Sigma^-$ is required", "type" : "info"}
        s_dict[3] = { "meaning" : "a $\Lambda$ or $\\bar{\Lambda}$ is required", "type" : "info"}
        s_dict[4] = { "meaning" : "a $K_S^0$ is required", "type" : "info"}
        s_dict[5] = { "meaning" : "an $\Omega^-$ or $\Omega^+$ is required", "type" : "info"}
        s_dict[6] = { "meaning" : "a Ξ − or Ξ + is required", "type" : "info"}
        s_dict[7] = { "meaning" : "a $K^-$ or $K^+$ is required", "type" : "info"}
        s_dict[8] = { "meaning" : "a $K_L^0$ is required", "type" : "info"}
        s_dict[9] = { "meaning" : "reserve", "type" : "error"}

    elif g_flag == 4:
        s_dict[0] = { "meaning" : "a Higgs is required", "type" : "info"}
        s_dict[1] = { "meaning" : "a t quark is required", "type" : "info"}
        s_dict[2] = { "meaning" : "a W or a Z is required", "type" : "info"}
        s_dict[3] = { "meaning" : "a Hidden Valley through Higgs is required", "type" : "info"}
        s_dict[4] = { "meaning" : "a Hidden Valley with multi v-pion is required", "type" : "info"}
        s_dict[5] = { "meaning" : "reserve", "type" : "error"}
        s_dict[6] = { "meaning" : "reserve", "type" : "error"}
        s_dict[7] = { "meaning" : "reserve", "type" : "error"}
        s_dict[8] = { "meaning" : "reserve", "type" : "error"}
        s_dict[9] = { "meaning" : "reserve", "type" : "error"}

    elif g_flag == 5:
        s_dict[0] = { "meaning" : "not used", "type" : "error" }
        s_dict[1] = { "meaning" : "e − particle gun", "type" : "info" }
        s_dict[2] = { "meaning" : "μ − particle gun", "type" : "info" }
        s_dict[3] = { "meaning" : "π + particle gun", "type" : "info" }
        s_dict[4] = { "meaning" : "K + particle gun", "type" : "error" }
        s_dict[5] = { "meaning" : "proton particle gun", "type" : "info" }
        s_dict[6] = { "meaning" : "γ particle gun", "type" : "info" }
        s_dict[7] = { "meaning" : "π 0 particle gun", "type" : "info" }
        s_dict[8] = { "meaning" : "geantinos particle gun", "type" : "info" }
        s_dict[9] = { "meaning" : "other particle type", "type" : "info" }
    elif g_flag == 6:
        s_dict[0] = { "meaning" : "no particular type of particle generated (i.e. all available types)", "type" : "info"}
        s_dict[1] = { "meaning" : "reserve", "type" : "error"}
        s_dict[2] = { "meaning" : "$\mu^{\pm}$ only generated", "type" : "info"}
        s_dict[3] = { "meaning" : "reserve", "type" : "error"}
        s_dict[4] = { "meaning" : "reserve", "type" : "error"}
        s_dict[5] = { "meaning" : "reserve", "type" : "error"}
        s_dict[6] = { "meaning" : "reserve", "type" : "error"}
        s_dict[7] = { "meaning" : "reserve", "type" : "error"}
        s_dict[8] = { "meaning" : "reserve", "type" : "error"}
        s_dict[9] = { "meaning" : "hadrons generated", "type" : "info"}
    return s_dict

def get_s_info(s_flag, g_flag):
    s_dict = get_s_info_dict(g_flag=g_flag)
    if s_flag not in s_dict.keys():
        return { "meaning" : "no fitting g flag", "type" : "error"}
    else:
        return s_dict[s_flag]

def get_d_info_dict(g_flag, c_flag, s_flag):
    d_dict = {}
    if g_flag in [1, 2, 3, 4]:
        d_dict[0] = { "meaning" : "No decay is forced (fully inclusive mode)", "type" : "info"}
        d_dict[1] = { "meaning" : "The selected particle(s) is(are) forced to decay to a unique exclusive final state, with a unique intermediate state (if any)", "type" : "info" }
        d_dict[2] = { "meaning" : "The selected particle(s) is(are) forced to decay to a unique exclusive final state, with multiple intermediate states", "type" : "info" }
        d_dict[3] = { "meaning" : "The selected particle(s) is(are) forced to decay to one of several exclusive final states (explicitely specified in a list) with identical topology", "type" : "info" }
        d_dict[4] = { "meaning" : "The selected particle(s) is(are) forced to decay to one of several exclusive final states (explicitely specified in a list) with different topologies", "type" : "info" }
        d_dict[5] = { "meaning" : "The selected particle(s) is(are) forced to decay to a unique exclusive final state, with a unique intermediate state (if any), but the final state(s) contain(s) at least one particle which cannot be measured (neutrinos)", "type" : "info" }
        d_dict[6] = { "meaning" : "The selected particle(s) is(are) forced to decay to a unique exclusive final state, with multiple intermediate states, but the final state(s) contain(s) at least one particle which cannot be measured (neutrinos)", "type" : "info" }
        d_dict[7] = { "meaning" : "The selected particle(s) is(are) forced to decay to one of several exclusive final states (explicitely specified in a list) with identical topology, but the final state(s) contain(s) at least one particle which cannot be measured (neutrinos)", "type" : "info" }
        d_dict[8] = { "meaning" : "The selected particle(s) is(are) forced to decay to one of several exclusive final states (explicitely specified in a list) with different topologies, but the final state(s) contain(s) at least one particle which cannot be measured (neutrinos)", "type" : "info" }
        d_dict[9] = { "meaning" : "The selected particle(s) is(are) forced to a decay chain containing some inclusive decays (semi-inclusive mode), resulting in a number of different final states which are not explicitely specified", "type" : "info" }
    elif g_flag == 5 and s_flag in [1,2,3,4,5,6,7]:
        d_dict[0] = { "meaning" : "particle", "type" : "info"}
        d_dict[1] = { "meaning" : "anti-particle", "type" : "info"}
        d_dict[2] = { "meaning" : "more than one particle", "type" : "info"}
        d_dict[3] = { "meaning" : "reserve", "type" : "error"}
        d_dict[4] = { "meaning" : "reserve", "type" : "error"}
        d_dict[5] = { "meaning" : "reserve", "type" : "error"}
        d_dict[6] = { "meaning" : "reserve", "type" : "error"}
        d_dict[7] = { "meaning" : "reserve", "type" : "error"}
        d_dict[8] = { "meaning" : "reserve", "type" : "error"}
        d_dict[9] = { "meaning" : "reserve", "type" : "error"}
    elif g_flag == 5 and s_flag == 9:
        d_dict[0] = { "meaning" : "reserve", "type" : "error"}
        d_dict[1] = { "meaning" : "J/ψ → μμ", "type" : "info"}
        d_dict[2] = { "meaning" : "reserve", "type" : "error"}
        d_dict[3] = { "meaning" : "reserve", "type" : "error"}
        d_dict[4] = { "meaning" : "reserve", "type" : "error"}
        d_dict[5] = { "meaning" : "reserve", "type" : "error"}
        d_dict[6] = { "meaning" : "reserve", "type" : "error"}
        d_dict[7] = { "meaning" : "reserve", "type" : "error"}
        d_dict[8] = { "meaning" : "reserve", "type" : "error"}
        d_dict[9] = { "meaning" : "reserve", "type" : "error"}
    elif g_flag == 6 and c_flag in [0,1]:
        d_dict[0] = { "meaning" : "gaussian p-Gas vertex distribution in x,y, uniform in z", "type" : "info"}
        d_dict[1] = { "meaning" : "uniform p-Gas vertex distribution in x,y and z", "type" :"info"}
        d_dict[2] = { "meaning" : "reserve", "type" : "error"}
        d_dict[3] = { "meaning" : "reserve", "type" : "error"}
        d_dict[4] = { "meaning" : "reserve", "type" : "error"}
        d_dict[5] = { "meaning" : "reserve", "type" : "error"}
        d_dict[6] = { "meaning" : "reserve", "type" : "error"}
        d_dict[7] = { "meaning" : "reserve", "type" : "error"}
        d_dict[8] = { "meaning" : "reserve", "type" : "error"}
        d_dict[9] = { "meaning" : "reserve", "type" : "error"}
    elif g_flag ==6 and c_flag ==5:
        d_dict[0] = {"meaning" : "staged shield, loss on TCTV.4L8.B1 & TCTH.L8.B1", "type" : "info" }
        d_dict[1] = {"meaning" : "staged shield, loss on TCTV.4L8.B1", "type" : "info" }
        d_dict[2] = {"meaning" : "staged shield, loss on TCTH.L8.B1", "type" : "info" }
        d_dict[3] = {"meaning" : "design shield, loss on TCTV.4L8.B1 & TCTH.L8.B1", "type" : "info" }
        d_dict[4] = {"meaning" : "design shield, loss on TCTV.4L8.B1", "type" : "info" }
        d_dict[5] = {"meaning" : "design shield, loss on TCTH.L8.B1", "type" : "info" }
        d_dict[6] = {"meaning" : "no shield, loss on TCTV.4L8.B1 & TCTH.L8.B1", "type" : "info" }
        d_dict[7] = {"meaning" : "no shield, loss on TCTH.L8.B1", "type" : "info" }
        d_dict[8] = {"meaning" : "no shield, loss on TCTH.L8.B1", "type" : "info" }
        d_dict[9] = {"meaning" : "reserve", "type" : "error"}
    return d_dict

def get_d_info(d_flag, g_flag, c_flag, s_flag):
    d_dict = get_d_info_dict(g_flag=g_flag, c_flag=c_flag, s_flag=s_flag)
    if d_flag not in d_dict.keys():
        return { "meaning" : "no fitting g flag", "type" : "error"}
    else:
        return d_dict[d_flag]

def get_c_info_dict(g_flag):
    c_dict = {}
    if g_flag in [1,2,3,4]:
        # When the general flag is equal to 1, 2, 3 or 4, this flag gives information on the presence or absence
        # of charm hadrons, electrons and muons present in the forced part of the decay chain of the selected
        # particle(s), as defined by the decay and selection flags. The inclusive part of the decay chain is not
        # considered. This flag is useful to determine the presence of a tertiary vertex from the weak decay
        # of a charm hadron. It is also useful to distinguish channels based on some of their triggering
        # signatures (fully hadronic modes, and modes with muons or electrons). Given the signal particle
        # is flagged elsewhere, the charm content of the signal particle does not trigger the charm-and-
        # lepton flag (Such as D ∗ and Jpsi signal particles).
        c_dict[0] = {"meaning" : "no $c\\bar{c}$ meson, no open-charm hadron, no muon no electron", "type" : "info"}
        c_dict[1] = {"meaning" : "no $c\\bar{c}$ meson, no open-charm hadron, at least 1 muon", "type" : "info"}
        c_dict[2] = {"meaning" : "no $c\\bar{c}$ meson, no open-charm hadron, no muon , electron : at least 1", "type" : "info"}

        c_dict[3] = {"meaning" : "at least 1 $c\\bar{c}$ meson, no open-charm hadron, no muon , no electron", "type" : "info"}
        c_dict[4] = {"meaning" : "at least 1 $c\\bar{c}$ meson, no open-charm hadron, at least 1 muon", "type" : "info"}
        c_dict[5] = {"meaning" : "at least 1 $c\\bar{c}$ meson, no open-charm hadron, no muon , at least 1 electron ", "type" : "info"}

        c_dict[6] = {"meaning" : "one open-charm hadron, no muon, no electron", "type" : "info"}
        c_dict[7] = {"meaning" : "at least one open-charm hadron, at least 1 muon", "type" : "info"}
        c_dict[8] = {"meaning" : "at least one open-charm hadron, no muon, at least 1 electron", "type" : "info"}

        c_dict[9] = {"meaning" : "at least 2 open-charm hadrons, no muon, no electron", "type" : "info"}

    elif g_flag == 5:
        c_dict[0] =  {"meaning" : "fixed momentum (specified in other flags) in calo acceptance", "type" : "info"}
        c_dict[1] =  {"meaning" : "fixed momentum (specified in other flags) in trackers acceptance", "type" : "info"}
        c_dict[2] =  {"meaning" : "reserve", "type" : "error"}
        c_dict[3] =  {"meaning" : "momentum range in calo acceptance", "type" : "info"}
        c_dict[4] =  {"meaning" : "momentum range in trackers acceptance", "type" : "info"}
        c_dict[5] =  {"meaning" : "flat $\eta$ (range specified in other flags) or flat x-y, flag set to 5", "type" : "info"}
        c_dict[6] =  {"meaning" : "flat $\eta$ (range specified in other flags) or flat x-y, flag set to 6", "type" : "info"}
        c_dict[7] =  {"meaning" : "flat $\eta$ (range specified in other flags) or flat x-y, flag set to 7", "type" : "info"}
        c_dict[8] =  {"meaning" : "flat $\eta$ (range specified in other flags) or flat x-y, flag set to 8", "type" : "info"}
        c_dict[9] =  {"meaning" : "flat $\eta$ (range specified in other flags) or flat x-y, flag set to 9", "type" : "info"}

    elif g_flag == 6:
        c_dict[0] = {"meaning" : "beam gas in VeLo" , "type" : "info" }
        c_dict[1] = {"meaning" : "beam gas in VeLo and beam pipe" , "type" : "info" }
        c_dict[2] = {"meaning" : "beam gas in IR8 Long Straight Section (LSS)" , "type" : "info" }
        c_dict[3] = {"meaning" : "beam gas in Arc" , "type" : "info" }
        c_dict[4] = {"meaning" : "beam gas in LSS and Arc" , "type" : "info" }
        c_dict[5] = {"meaning" : "halo on Collimators" , "type" : "info" }
        c_dict[6] =  {"meaning" : "reserve", "type" : "error"}
        c_dict[7] =  {"meaning" : "reserve", "type" : "error"}
        c_dict[8] =  {"meaning" : "reserve", "type" : "error"}
        c_dict[9] =  {"meaning" : "reserve", "type" : "error"}

    return c_dict

def get_c_info(c_flag, g_flag):
    c_dict = get_c_info_dict(g_flag=g_flag)
    if c_flag not in c_dict.keys():
        return { "meaning" : "no fitting g flag", "type" : "error"}
    else:
        return c_dict[c_flag]



def get_t_info(t_flag, g_flag, c_flag):
    # The track flag is equal to the total number of “stable” charged particles in the forced part of the
    # decay chain(s) of the selected particle(s). The forced part of the decay chain(s) is as defined by
    # the decay flag, and the selected particle(s) are those involved in the definition of the selection
    # flag. Only the following charged particles are counted: protons, charged pions, charged kaons,
    # electrons and muons (tracks from K S 0 and Λ decays are counted). If the count is larger than 9,
    # then the flag is set to 9. The value 0 is possible. If the decay flag is 3, 4, 7 or 8, the assignment of
    # the track flag may become ambiguous. In that case, tracks should be counted using the dominant
    # or more representative forced decay chain.
    if g_flag == 6 :
        t_dict = {}
        t_dict[0] = {"meaning" : "both beams", "type" : "info"}
        t_dict[1] = {"meaning" : "beam 1 (traveling from VeLo to Muon system)", "type" : "info"}
        t_dict[2] = {"meaning" : "beam 2 (traveling from Muon system to VeLo)", "type" : "info"}
        t_dict[3] =  {"meaning" : "reserve", "type" : "error"}
        t_dict[4] =  {"meaning" : "reserve", "type" : "error"}
        t_dict[5] =  {"meaning" : "reserve", "type" : "error"}
        t_dict[6] =  {"meaning" : "reserve", "type" : "error"}
        t_dict[7] =  {"meaning" : "reserve", "type" : "error"}
        t_dict[8] =  {"meaning" : "reserve", "type" : "error"}
        t_dict[9] =  {"meaning" : "reserve", "type" : "error"}
	return t_dict[t_flag]
    elif g_flag == 5: 
            if c_flag == 0:
                return {"meaning" : "first digit of the four-digit value of the momentum of the particle (The momentum is given in GeV,rounded up)", "type" : "info"}
            elif c_flag == 1:
                return {"meaning" : "first digit of the two-digit minimum value of the $\eta$ range", "type" : "info"}
            elif c_flag in [2,3]:
                return {"meaning" : "flag must be zero", "type" : "info"}
            else:
                return {"meaning" : "reserve", "type" : "error"}
    else:
        if t_flag < 9:
            return {"meaning" : str(t_flag) + " “stable” charged particles in the forced part of the decay chain(s) of the selected particle(s)", "type" : "info"}
        else:
            return {"meaning" : "At least 9  “stable” charged particles in the forced part of the decay chain(s) of the selected particle(s)", "type" : "info"}



def get_n_info(n_flag, g_flag, c_flag, s_flag):
    # The neutral flag indicated the presence of certain neutral particles in the forced part of the decay
    # chain(s) of the selected particle(s). The forced part of the decay chain(s) is as defined by the decay
    # flag, and the selected particle(s) are those involved in the definition of the selection flag. The
    # following neutral or ECAL particles are considered: K S 0 or Λ decaying to two charged hadrons,
    # γ (excluding photons from π 0 → γγ and η → γγ decays and radiative photons such as photons
    # produced by PHOTOS for example in J/ψ → l + l − γ), π 0 and η decaying to two photons, and
    # neutron and K L 0 . The π 0 and η particles are flagged even if they are not explicitly decayed in the
    # decay file but left to decay according to DECAY.DEC. The neutral flag is bit-coded according to
    # Table 10. If the decay flag is 3, 4, 7 or 8, the assignment of the neutral flag may become ambiguous.
    # In that case, the neutral flag should be determined using the dominant or more representative
    # forced decay chain.
    if g_flag == 6 and c_flag in [0,1]:  
        return  {"meaning" : "label indicates gas type", "type" : "info"}
    elif g_flag == 5: 
            if c_flag == 0:
                return {"meaning" : "second digit of the four-digit value of the momentum of the particle (The momentum is given in GeV,rounded up)", "type" : "info"}
            elif c_flag == 1:
                return {"meaning" : "second digit of the two-digit minimum value of the $\eta$ range", "type" : "info"}
            elif c_flag in [2,3]:
                return {"meaning" : "flag must be zero", "type" : "info"}
            else:
                return {"meaning" : "reserve", "type" : "error"}
    else:
        meaning = []
        binary = "{0:b}".format(n_flag).zfill(4)
        if binary[-1] == "1":
            meaning += ["at least one $K_S^0 \\to \pi^+ \pi^-$, $\Lambda \\to p \pi^-$ or  $\Lambda \\to \\bar{p} \pi^+$"]
        if binary[-2] == "1":
            meaning += ["at least one $\gamma$ not from $\pi^0 \\to \gamma \gamma$, $\eta \\to \gamma \gamma$ nor a radiative photon "]
        if binary[-3] == "1":
            meaning += ["at least one $\pi_0 \\to \gamma \gamma$ or $\eta \\to \gamma \gamma $"]
        if binary[-4] == "1":
            meaning += [" at least one neutron or $K_L^0$"]
        if not meaning:
            return{ "meaning" : " certain neutral decays are not present in the decay chain", "type" : "info"}
        else:
            return{ "meaning" : " AND ".join(meaning), "type" : "info"}


def get_x_info_dict(g_flag, s_flag):
    x_dict = {}
    if g_flag == 1 and s_flag == 6 :
        x_dict[0] = { "meaning" : "a Σ −b or Σ̄ b is required", "type" : "info"}
        x_dict[1] = { "meaning" : "a Σ b or Σ̄ b is required", "type" : "info"}
        x_dict[2] = { "meaning" : "a Σ +b or Σ̄ b is required", "type" : "info"}
        x_dict[3] = { "meaning" : "a Ξ b or Ξ̄ b is required", "type" : "info"}
        x_dict[4] = { "meaning" : "a Ξ 0 b or Ξ̄ 0 b is required", "type" : "info"}
        x_dict[5] = { "meaning" : "a Ω −b or Ω̄ b is required", "type" : "info"}
        x_dict[6] = { "meaning" : "a bc baryon is required", "type" : "info"}
        x_dict[7] = { "meaning" : "a bb baryon is required", "type" : "info"}
        x_dict[8] = { "meaning" : "reserve", "type" : "error"}
        x_dict[9] = { "meaning" : "all other b baryons", "type" : "info"}

    elif g_flag == 1 and s_flag==7 : 
        x_dict[0] = { "meaning" : "a B ∗0 or B̄ ∗0 is required", "type" : "info"}
        x_dict[1] = { "meaning" : "a B ∗+ or B ∗− is required", "type" : "info"}
        x_dict[2] = { "meaning" : "a B s ∗0 or B̄ s ∗0 is required", "type" : "info"}
        x_dict[3] = { "meaning" : "a B 1 0 (L) or B̄ 1 0 (L) is required", "type" : "info"}
        x_dict[4] = { "meaning" : "a B 1 + (L) or B 1 − (L) is required", "type" : "info"}
        x_dict[5] = { "meaning" : "a B s1 (L) or B̄ s1 (L) is required", "type" : "info"}
        x_dict[6] = { "meaning" : "a B 2 (L) or B̄ 2 ∗0 (L) is required", "type" : "info"}
        x_dict[7] = { "meaning" : "a B 2 ∗+ (L) or B 2 ∗− (L) is required", "type" : "info"}
        x_dict[8] = { "meaning" : "a B (L) or B̄ s2 is required", "type" : "info"}
        x_dict[9] = { "meaning" : "reserve", "type" : "error"}

    elif g_flag == 1 and s_flag==8 : 
        x_dict[0] = { "meaning" : "a Υ(1S) is required", "type" : "info"}
        x_dict[1] = { "meaning" : "a Υ(2S) is required", "type" : "info"}
        x_dict[2] = { "meaning" : "a Υ(3S) is required", "type" : "info"}
        x_dict[3] = { "meaning" : "a Υ(4S) is required", "type" : "info"}
        x_dict[4] = { "meaning" : "a Υ(5S) is required", "type" : "info"}
        x_dict[5] = { "meaning" : "a χ b0 (1P ) is required", "type" : "info"}
        x_dict[6] = { "meaning" : "a χ b1 (1P ) is required", "type" : "info"}
        x_dict[7] = { "meaning" : "a χ b2 (1P ) is required", "type" : "info"}
        x_dict[8] = { "meaning" : "reserve", "type" : "error"}
        x_dict[9] = { "meaning" : "reserve", "type" : "error"}

    elif g_flag == 2 and s_flag == 6 :
        x_dict[0] = { "meaning" : "a Σ 0 c or Σ̄ 0 c is required" , "type" : "info"}
        x_dict[1] = { "meaning" : "reserved" , "type" : "error"}
        x_dict[2] = { "meaning" : "a Σ ++ or Σ̄ −−is required" , "type" : "info"}
        x_dict[3] = { "meaning" : "a Σ c or Σ̄ ∗0c is required" , "type" : "info"}
        x_dict[4] = { "meaning" : "a Σ ∗++ or Σ̄ ∗−− is required" , "type" : "info"}
        x_dict[5] = { "meaning" : "a Ξ cc or Ξ̄ − cc is required" , "type" : "info"}
        x_dict[6] = { "meaning" : "a Ξ ++ cc or Ξ̄ cc is required" , "type" : "info"}
        x_dict[7] = { "meaning" : "reserve", "type" : "error"}
        x_dict[8] = { "meaning" : "reserve", "type" : "error"}
        x_dict[9] = { "meaning" : "reserve", "type" : "error"}

    elif g_flag == 2 and s_flag == 7 :
        x_dict[0] = { "meaning" : "a D ∗+ or D ∗− is required", "type" : "info" }
        x_dict[1] = { "meaning" : "a D ∗0 or D̄ ∗0 is required", "type" : "info" }
        x_dict[2] = { "meaning" : "a D s ∗+ or D s ∗− is required", "type" : "info" }
        x_dict[3] = { "meaning" : "a D s2(2536) + or D s2(2536) − is required", "type" : "info" }
        x_dict[4] = { "meaning" : "a D 2 (2460) or D̄ 2 (2460) − is required", "type" : "info" }
        x_dict[5] = { "meaning" : "a D 2 ∗ (2460) + or D 2 ∗ (2460) − is required", "type" : "info" }
        x_dict[6] = { "meaning" : "a D s1 (2460) + or D s1 (2460) − is required", "type" : "info" }
        x_dict[7] = { "meaning" : "a D ∗+ or D ∗− is required", "type" : "info" }
        x_dict[8] = { "meaning" : "reserve", "type" : "error"}
        x_dict[9] = { "meaning" : "reserve", "type" : "error"}

    elif g_flag == 2 and s_flag == 8 :
        x_dict[0] = { "meaning" : "a ψ(2S) is required", "type" : "info"}
        x_dict[1] = { "meaning" : "a X(3872) is required", "type" : "info"}
        x_dict[2] = { "meaning" : "a h c is required", "type" : "info"}
        x_dict[3] = { "meaning" : "a χ c0 is required", "type" : "info"}
        x_dict[4] = { "meaning" : "a χ c1 is required", "type" : "info"}
        x_dict[5] = { "meaning" : "a χ c2 is required", "type" : "info"}
        x_dict[6] = { "meaning" : "a η c (1S) is required", "type" : "info"}
        x_dict[7] = { "meaning" : "a ψ(3770) is required", "type" : "info"}
        x_dict[8] = { "meaning" : "reserve", "type" : "error"}
        x_dict[9] = { "meaning" : "reserve", "type" : "error"}
    return x_dict

def get_x_info(x_flag, g_flag, s_flag):
    if g_flag == 5 and (t_flag!=0 or n_flag!=0) : 
        if c_flag == 0:
            return {"meaning" : "third digit of the four-digit value of the momentum of the particle (The momentum is given in GeV,rounded up)", "type" : "info"}
        elif c_flag == 1:
            return {"meaning" : "first digit of the two-digit maximum value of the $\eta$ range", "type" : "info"}
        else:
            return {"meaning" : "reserve", "type" : "error"}
    else:
        x_info_dict = get_x_info_dict(g_flag, s_flag)
        try:
            response =  x_info_dict[x_flag]
        except KeyError:
            response =  { "meaning" : "reserve", "type" : "error"}
        return response

def get_u_info():
    return { "meaning" : "reserved user flag indicating various different generator conditions.", "type" : "info"}
