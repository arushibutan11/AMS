
$("#id_CIRCLE").change(function () {
    var selection = $("#id_CIRCLE option:selected").text(); //grab the value selected
    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
    $.post({
        url: '/getcircleinfo',
        data: {
          'circle': selection
        },
        dataType: 'json',
        success: function (data) {
            document.getElementById("id_DIST").value = data['DIST'];
            document.getElementById("id_RNG").value = data['RANGE'];
        }
      });
    });




$("#id_PS, #id_DATE_OCC_year,  #id_FIRNO").change(function () {
    var ps =  document.getElementById("id_PS").value;
    var firno =  document.getElementById("id_FIRNO").value;
    firno =  parseInt(firno);
    var psCode = ps.split("-");
    var yr = document.getElementById("id_DATE_OCC_year").value;
    var id = document.getElementById("id_DATE_OCC_year").value +  psCode[1] +  firno;
    if(document.getElementById("id_FIRNO").value!="" && document.getElementById("id_PS").value!="" && document.getElementById("id_DATE_OCC_year").value!=0)
    { document.getElementById("id_ACC_ID").value = id;
      $('.iACCID_ID').val(id);
      $('.iPS').val(psCode[1]);
      $('.iYEAR').val(yr);
      $('.iFIRNO').val(firno);

    }
});

$('.vvic-formset').formset({
    addText: '<span class = "btn btn-success btn-sm">Add</span>',
    deleteText: '<span class = "btn btn-danger btn-sm">Remove</span>',
    prefix: 'vvic'
});
$('.pvic-formset').formset({
    addText: '<span class = "btn btn-success btn-sm">Add</span>',
    deleteText: '<span class = "btn btn-danger btn-sm">Remove</span>',
    prefix: 'pvic'

    });
$('.offend-formset').formset({
    addText: '<span class = "btn btn-success btn-sm">Add</span>',
    deleteText: '<span class = "btn btn-danger btn-sm">Remove</span>',
    prefix: 'offend'
});
$('.cause-formset').formset({
    addText: '<span class = "btn btn-success btn-sm">Add</span>',
    deleteText: '<span class = "btn btn-danger btn-sm">Remove</span>',
    prefix: 'cause'

    });



$(document).ready(function() {
  $('#id_ROAD').change(function() {
    var roadname = $("#id_ROAD option:selected").text();
    $("#id_ROADNAME").val(roadname).change();


  });
});
/*
$('div[id*="-VEHTYPE1"]').change(function(){
{
  var formid = this.attr('id'));

});
$("#id_VEHTYPE1").change(function () {
    var selection = $("#id_VEHTYPE1 option:selected").text();
    //alert("you selected" + selection);
    if (selection=='BUS DTC')
    {

     document.getElementById("route").style.visibility = "visible";
    $("#id_routeno").show();
    }
    else
    {
        document.getElementById("route").style.visibility = "hidden";
        //$("#id_routeno").attr('disabled', true);
         $("#id_routeno").hide()

    }
    if(selection=='TWW')
    {
      document.getElementById("tww1").style.visibility = "visible";
    $("#id_TWW1").show();
    }
    else
    {
        document.getElementById("tww1").style.visibility = "hidden";
        //$("#id_routeno").attr('disabled', true);
         $("#id_TWW1").hide()

    }
    if (selection=='ANIMAL'|| selection=='BULLOCK CARTS' || selection== 'CYCLIST'|| selection=='CYCLE RICKSHOW' ||selection== 'E RICKSHAW' || selection=='HAND CARTS'|| selection=='WALL' ||selection== 'ELECTRIC POLL' || selection== 'HTV/GOODS' ||selection== 'PEDESTRIAN' ||selection== 'SELF')
    {
        document.getElementById("RNOV1A").style.visibility = "hidden";
        document.getElementById("RNOV1B").style.visibility = "hidden";
        //$("#id_routeno").attr('disabled', true);
        $("#id_RNOV1A").hide()
        $("#id_RNOV1B").hide()
    }
    else
    {
        document.getElementById("RNOV1A").style.visibility = "visible";
        document.getElementById("RNOV1B").style.visibility = "visible";
        $("#id_RNOV1A").show();
        $("#id_RNOV1B").show();
    }

    });

$("#id_VEHTYPE2").change(function () {
    var selection = $("#id_VEHTYPE2 option:selected").text();
    //if selection == "PED" && (VICTIM1 = "VEHICLES" Or VICTIM1 = "SELF" Or VICTIM1 = "PASSENGER" Or VICTIM1 = "SELF/ANIMAL")
    if (selection=='SELF')
    {
     $("#self_type").show();
    $("#id_SELF_TYPE").show();
    }
    else
    {
        $("#self_type").hide();
        //$("#id_routeno").attr('disabled', true);
         $("#id_SELF_TYPE").hide()

    }
     if (selection=='PEDESTRIAN')
    {
     document.getElementById("Pedestrian").style.visibility = "visible";
    $("#id_PEDESTRIAN").show();
    }

    else
    {
        document.getElementById("Pedestrian").style.visibility = "hidden";
        //$("#id_routeno").attr('disabled', true);
         $("#id_PEDESTRIAN").hide()

    }
      if (selection=='ANIMAL'|| selection=='BULLOCK CARTS' || selection== 'CYCLIST'|| selection=='CYCLE RICKSHOW' ||selection== 'E RICKSHAW' || selection=='HAND CARTS'|| selection=='WALL' ||selection== 'ELECTRIC POLL' || selection== 'HTV/GOODS' ||selection== 'PEDESTRIAN' ||selection== 'SELF' || selection=='PASSENGER' || selection=='CYCLE')
    {
        document.getElementById("RNOV2A").style.visibility = "hidden";
        document.getElementById("RNOV2B").style.visibility = "hidden";
        //$("#id_routeno").attr('disabled', true);
        $("#id_RNOV2A").hide()
        $("#id_RNOV2B").hide()
    }
    else
    {
        document.getElementById("RNOV2A").style.visibility = "visible";
        document.getElementById("RNOV2B").style.visibility = "visible";
        $("#id_RNOV2A").show();
        $("#id_RNOV2B").show();
    }



  }); */
