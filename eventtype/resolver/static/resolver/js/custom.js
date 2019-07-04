/*****************************************************************************\
* (c) Copyright 2016-2019 CERN for the benefit of the LHCb Collaboration      *
*                                                                             *
* This software is distributed under the terms of the GNU General Public      *
* Licence version 3 (GPL Version 3), copied verbatim in the file "COPYING".   *
*                                                                             *
* In applying this licence, CERN does not waive the privileges and immunities *
* granted to it by virtue of its status as an Intergovernmental Organization  *
* or submit itself to any jurisdiction.                                       *
\*****************************************************************************/

window.addEventListener('message', function(event) {
    if ( "pennytoken-protocol-version" in event.data){
        console.log('page javascript got message');
        $(".plugin_not_present").hide();
        $(".plugin_present").show();
    }
});


// Sets active link in Bootstrap menu
// Add this code in a central place used\shared by all pages
// like your _Layout.cshtml in ASP.NET MVC for example
$('a[href="' + this.location.pathname + '"]').parents('li,ul').addClass('active');