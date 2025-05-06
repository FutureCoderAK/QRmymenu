(function($) {
    $(document).ready(function() {
        // أخفي الحقول عند تحميل الصفحة
        function hideFields() {
            $("#id_is_hide, #id_not_dound").closest('.form-row').hide();
        }

        hideFields();  // استدعاء الدالة لإخفاء الحقول عند تحميل الصفحة

        // عندما يتم تغيير خيار معين، قم بإظهار الحقول
        $("#id_main_category").change(function() {
            var value = $(this).val();
            
            if (value) {
                $("#id_is_hide, #id_not_dound").closest('.form-row').show(); // إظهار الحقول
            } else {
                hideFields();  // إخفاء الحقول إذا لم يتم اختيار شيء
            }
        });
    });
})(django.jQuery);
