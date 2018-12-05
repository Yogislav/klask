// Inicjalizacja różnych modułów JS
$(document).ready(function () {
  var url = document.location.toString()

  // Inicjalizacja modułu Bootstrap Confirmation (potwierdzenie wysłania formularza)
  $('[data-toggle=confirmation]').each(function() {
    $(this).confirmation({
      rootSelector: '[data-toggle=confirmation]',
    });
  });

  // Inicjalizac modułu Select2 (listy rozwijalne)
  $('select').select2({
    language: "pl",
    minimumResultsForSearch: 10,
    width: '100%'
  });
  
  $('.close').on('click', function(e) {
      $(e.target).parent().remove()
  });
});

// -=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-