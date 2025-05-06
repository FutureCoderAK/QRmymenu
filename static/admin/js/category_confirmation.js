// category_confirmation.js
(function() {
    const form = document.querySelector('form');
    const isDuplicate = document.querySelector('input[name="is_duplicate"]').value === 'True';

    if (isDuplicate) {
        form.addEventListener('submit', function(event) {
            const confirmMessage = "الاسم مكرر! هل أنت متأكد أنك تريد إضافة هذا العنصر؟";
            const userConfirmed = window.confirm(confirmMessage);

            if (!userConfirmed) {
                event.preventDefault();
            }
        });
    }
})();