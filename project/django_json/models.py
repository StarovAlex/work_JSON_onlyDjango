from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    parent = models.ForeignKey(to='Category', blank=True, null=True)

    def get_parent(self, items_list):
        if self.parent:
            category = Category.objects.get(pk=self.parent_id)
            items_list.append(category)
            if category.parent:
                category.get_parent(items_list)

    def get_children(self):
        return [item for item in self.category_set.all()]

    def get_sibling(self):
        return [item for item in Category.objects.filter(parent_id=self.parent_id).exclude(pk=self.pk)]
