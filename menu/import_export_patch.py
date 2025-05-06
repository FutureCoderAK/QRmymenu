from import_export.resources import ModelResource

class PatchedModelResource(ModelResource):
    def after_import_instance(self, instance, new, row_number=None, **kwargs):
        """
        نوقف تسجيل الـ Log عشان يتفادى مشكلة single_object
        """
        pass  # مفيش تسجيل أصلاً