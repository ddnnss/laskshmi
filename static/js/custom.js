(function($) {
  "use strict";

  function customQuantity() {
    /** Custom Input number increment js **/
    jQuery(
      '<div class="pt_QuantityNav"><div class="pt_QuantityButton pt_QuantityUp">+</div><div class="pt_QuantityButton pt_QuantityDown">-</div></div>'
    ).insertAfter(".pt_Quantity input");
    jQuery(".pt_Quantity").each(function() {
      var spinner = jQuery(this),
        input = spinner.find('input[type="number"]'),
        btnUp = spinner.find(".pt_QuantityUp"),
        btnDown = spinner.find(".pt_QuantityDown"),
        min = input.attr("min"),
        max = input.attr("max"),
        valOfAmout = input.val(),
        newVal = 0;

      btnUp.on("click", function() {
        var oldValue = parseFloat(input.val());

        if (oldValue >= max) {
          var newVal = oldValue;
        } else {
          var newVal = oldValue + 1;
        }
        spinner.find("input").val(newVal);
        spinner.find("input").trigger("change");
      });
      btnDown.on("click", function() {
        var oldValue = parseFloat(input.val());
        if (oldValue <= min) {
          var newVal = oldValue;
        } else {
          var newVal = oldValue - 1;
        }
        spinner.find("input").val(newVal);
        spinner.find("input").trigger("change");
      });
    });
  }
  customQuantity();
})(jQuery);
