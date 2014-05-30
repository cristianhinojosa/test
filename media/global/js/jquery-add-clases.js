$(document).ready(function(){
	$("form").addClass( "form-agregar-productos" );
	$(".form-agregar-productos input").addClass( "form-control" );
	$("#id_imagen_1").removeClass( "form-control" );
	
	
	
	$('#tabla_productos tr[data-href]').addClass('clickable').click( function() { 
        window.location = $(this).attr('data-href'); 
    }).find('a').hover( function() { 
        $(this).parents('tr').unbind('click'); 
    }, function() { 
        $(this).parents('tr').click( function() { 
            window.location = $(this).attr('data-href'); 
        }); 
    }); 

	
	
});

