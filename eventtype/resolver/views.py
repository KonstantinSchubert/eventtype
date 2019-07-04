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
from django.shortcuts import render
from resolver.event_type_parser import *
from django.template import loader, RequestContext
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"resolver/index.html")

def about(request):
    return render(request, "resolver/about.html")


def resolve(request):

    information = {}

    if "event_number_input" in request.GET:
        information["has_event_number"] = True
        event_number = request.GET["event_number_input"]

        information["event_number"] = event_number

        g = int(event_number[0])
        s = int(event_number[1])
        d = int(event_number[2])
        c = int(event_number[3])
        t = int(event_number[4])
        n = int(event_number[5])
        x = int(event_number[6])
        u = int(event_number[7])

        information["g"] = get_g_info(g)
        information["s"] = get_s_info(s_flag=s, g_flag=g)
        information["d"] = get_d_info(d_flag=d, g_flag=g, c_flag=c, s_flag=s)
        information["c"] = get_c_info(c_flag=c, g_flag=g)
        information["t"] = get_t_info(t_flag=t, g_flag=g, c_flag=c)
        information["n"] = get_n_info(n_flag=n, g_flag=g, c_flag=c, s_flag=s)
        information["x"] = get_x_info(x_flag=x, g_flag=g, s_flag=s)
        information["u"] = get_u_info()

        information["g"]["flag"] = g
        information["s"]["flag"] = s
        information["d"]["flag"] = d
        information["c"]["flag"] = c
        information["t"]["flag"] = t
        information["n"]["flag"] = n
        information["x"]["flag"] = x
        information["u"]["flag"] = u
    else:
        information["has_event_number"] = False

    template = loader.get_template('resolver/resolve.html')
    context = RequestContext(request, information)
    return HttpResponse(template.render(context))


def builder(request):

    # first we build a dict of the flags we already figure out
    request_get = request.GET.dict()

    if "g_flag" not in request_get.keys():
        # this is the easiest flag to figure out.
        single_choice = [
            {"name" : 1, "meaning" : "Event contains a b quark, extracted from a minimum bias sample"},
            {"name" : 2, "meaning" : "Event contains a c quark, extracted from a minimum bias sample"},
            {"name" : 3, "meaning" : "Other events, extracted from a minimum bias sample"},
            {"name" : 4, "meaning" : "non-flavour physics with special generator settings"},
            {"name" : 5, "meaning" : "particle guns"} ,
            {"name" : 6, "meaning" : "machine induced background (MIB) events"},
            {"name" : 9, "meaning" : "real data"}
        ]

        description = "Choose which of the following  choices applies to your decay."
        template = loader.get_template('builder/single_choice.html')
        context = RequestContext(request, {
                                            "single_choice" : single_choice, 
                                            "description" : description, 
                                            "flag_name" : "g_flag", 
                                            "get_dict" : request_get.items(),
                                            "request_get" : request_get,
                                            })
        return HttpResponse(template.render(context))

    if "s_flag" not in request_get.keys() and "g_flag" in request_get.keys():
        s_choices = get_s_info_dict(g_flag=int(request_get["g_flag"]))
        single_choice = []
        for s_flag, values in s_choices.items():
            if values["type"] == "info":
                single_choice.append({"name" : s_flag, "meaning" : values["meaning"]})
        description = "Choose which of the following choices applies to your decay."
        template = loader.get_template('builder/single_choice.html')
        context = RequestContext(request, {
                                            "single_choice" : single_choice, 
                                            "description" : description, 
                                            "flag_name" : "s_flag", 
                                            "get_dict" : request_get.items(),
                                            "request_get" : request_get,
                                            })
        return HttpResponse(template.render(context))


    if "c_flag" not in request_get.keys() and "g_flag" in request_get.keys():
        c_choices = get_c_info_dict(g_flag=int(request_get["g_flag"]))
        single_choice = []
        for flag, values in c_choices.items():
            if values["type"] == "info":
                single_choice.append({"name" : flag, "meaning" : values["meaning"]})
        description = "Choose which of the following choices applies to your decay."
        template = loader.get_template('builder/single_choice.html')
        context = RequestContext(request, {
                                            "single_choice" : single_choice, 
                                            "description" : description, 
                                            "flag_name" : "c_flag", 
                                            "get_dict" : request_get.items(),
                                            "request_get" : request_get,
                                            })
        return HttpResponse(template.render(context))

    if "d_flag" not in request_get.keys() and "c_flag" in request_get.keys() and "g_flag" in request_get.keys() and "s_flag" in request_get.keys():
        d_choices = get_d_info_dict(g_flag=int(request_get["g_flag"]), c_flag=int(request_get["c_flag"]), s_flag=int(request_get["s_flag"]))
        single_choice = []
        for flag, values in d_choices.items():
            if values["type"] == "info":
                single_choice.append({"name" : flag, "meaning" : values["meaning"]})
        #shortcut if there is only one option
        if len(single_choice) == 1: 
            request_get["d_flag"] = single_choice[0]["name"]
        else:
            description = "Choose which of the following choices applies to your decay."
            template = loader.get_template('builder/single_choice.html')
            context = RequestContext(request, {
                                                "single_choice" : single_choice, 
                                                "description" : description, 
                                                "flag_name" : "d_flag", 
                                                "get_dict" : request_get.items(),
                                                "request_get" : request_get,
                                                })
            return HttpResponse(template.render(context))

    if "t_flag" not in request_get.keys() and "c_flag" in request_get.keys() and "g_flag" in request_get.keys():
        if request_get["g_flag"] == "6" :
            single_choice = [
                {"meaning" : "Events are produced for both beams", "name" : "0"},
                {"meaning" : "Events are produced for beam 1 (traveling from VeLo to Muon system)", "name" : "1"},
                {"meaning" : "Events are produced for beam 2 (traveling from Muon system to VeLo)", "name" : "2"}
            ]
            template = loader.get_template('builder/single_choice.html')
            context = RequestContext(request, {
                                            "single_choice" : single_choice, 
                                            "description" : "Choose which of the following choices applies to your decay.", 
                                            "flag_name" : "t_flag", 
                                            "get_dict" : request_get.items(),
                                            "request_get" : request_get,
                                            })
            return HttpResponse(template.render(context))
            
        elif request_get["g_flag"] == "5": 
                if request_get["c_flag"] == "0":
                    template = loader.get_template('builder/get_four_momentum.html') #gives the last 4 digits -> afterwards we are done
                    # get the four-digit value of the momentum of the particle (The momentum is given in GeV,rounded up)
                    context = RequestContext(request, {
                                                        "get_dict" : request_get.items(),
                                                        "request_get" : request_get
                                                    })
                    return HttpResponse(template.render(context))

                elif request_get["c_flag"] == "1":
                    template = loader.get_template('builder/get_eta_range.html') #gives the last 4 digits -> afterwards we are done
                    context = RequestContext(request, {
                                                "get_dict" : request_get.items(),
                                                "request_get" : request_get
                                            })
                    return HttpResponse(template.render(context))
                elif request_get["c_flag"] in ["2","3"]:
                    # "flag must be zero"
                    request_get["t_flag"] = "0"
                    request_get["n_flag"] = "0"
                else:
                    pass # the flag is not defined
        else:
            template = loader.get_template('builder/get_number_charged_particles.html')
            context = RequestContext(request, {
                                        "get_dict" : request_get.items(),
                                        "request_get" : request_get
                                    })
            return HttpResponse(template.render(context))
    if "n_flag" not in request_get.keys() and  "g_flag" in request_get.keys()  and "c_flag" in request_get.keys() and "s_flag" in request_get.keys():
        if request_get["g_flag"] == "6" and request_get["c_flag"] in ["0","1"]:  
            template = loader.get_template('builder/get_gas_type.html') 
            context = RequestContext(request, { 
                                                    "get_dict" : request_get.items(),
                                                    "request_get" : request_get
                                                })
            return HttpResponse(template.render(context))
            
        elif request_get["g_flag"] == "5" and request_get["c_flag"] in [2,3]:
            request_get["n_flag"] = "0"
        else:
            template = loader.get_template('builder/get_neutral_decays.html')
            context = RequestContext(request, {
                                            "get_dict" : request_get.items(),
                                            "request_get" : request_get
                                            })
            return HttpResponse(template.render(context))

    if "x_flag" not in request_get.keys() and "g_flag" in request_get.keys() and "s_flag" in request_get.keys() and "n_flag" in request_get.keys() and "t_flag" in request_get.keys():
        if not (request_get["g_flag"] == "5" and (request_get["t_flag"] != "0" or request_get["n_flag"] != "0")):
            x_choices = get_x_info_dict(g_flag=int(request_get["g_flag"]), s_flag=int(request_get["s_flag"]))
            if x_choices:
                single_choice = []
                for flag, values in x_choices.items():
                    if values["type"] == "info":
                        single_choice.append({"name" : flag, "meaning" : values["meaning"]})
                template = loader.get_template('builder/single_choice.html')
                context = RequestContext(request, {
                                                    "single_choice" : single_choice, 
                                                    "description" : "Choose which of the following choices applies to your decay.", 
                                                    "flag_name" : "x_flag", 
                                                    "get_dict" : request_get.items(),
                                                    "request_get" : request_get,
                                                    })
                return HttpResponse(template.render(context))            
    template = loader.get_template('builder/end.html')
    context = RequestContext(request, {"request_get" : request_get})
    return HttpResponse(template.render(context))

