


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


	
id_FIRNO.oninput = function () {
    if (this.value.length > 4) {
        this.value = this.value.slice(0,4); 
    }
}

\

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
$("#id_TIME_KNOWN_1") // select the radio by its id
    .change(function(){
			alert("yes");// bind a function to the change event
        if( $(this).is(":checked") ){ // check if the radio is checked
            var val = $(this).val();
				$('#id_TIME_0CC').css("display", "block");// retrieve the value
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
$('.collision-formset').formset({
    addText: '<span class = "btn btn-success btn-sm">Add</span>',
    deleteText: '<span class = "btn btn-danger btn-sm">Remove</span>',
    prefix: 'collision'
    
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


