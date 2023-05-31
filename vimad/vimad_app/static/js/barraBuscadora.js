$(document).ready(function() {
    $('#buscar-btn').click(function() {
        var query = $('#buscar-input').val();

        $.ajax({
            url: '/buscar/',
            data: {
                'q': query
            },
            dataType: 'json',
            success: function(data) {
                $('#resultados-busqueda').empty();

                if (data.cortos.length == 0) {
                    $('#resultados-busqueda').append('<p>No se encontraron resultados.</p>');
                } else {
                    $.each(data.cortos, function(index, corto) {
                        $('#resultados-busqueda').append('<a href="{% url "ficha" slug="' + corto.slug + '" %}" class="list-group-item list-group-item-action"><img src="' + corto.imagen + '" alt="Imagen del corto"><h5 class="mb-1">' + corto.titulo + '</h5><p class="mb-1">' + corto.genero + ', ' + corto.idioma + ', ' + corto.pais + '</p></a>');
                    });
                }
            }
        });
    });
});