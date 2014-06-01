$(document).ready(function(){
	/* $("form").addClass( "form-agregar-productos-2" ); */
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
    
 $("input[name='pregunta'], select[name='pregunta']", this).each(function() {
        if ($(this).val() === '' || $(this).val() === null) {
            
           $('#form_producto_respuesta').remove(); 
          
        /*	
         *  $(this).parent().parent().remove();
         * $('.form-agregar-productos').remove();*/
        }
    });


	
	
});

