from django.db import models
from django.contrib.auth.models import User
from pages.models import shoes,bags,menshirts,dresses,watches

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    details=models.ManyToManyField(menshirts, through='OrderDetails')
    is_finished = models.BooleanField()

    def __str__(self):
        return 'User: ' + self.user.username + ',Order id: ' + str(self.id)

class OrderDetails(models.Model):
        product=models.ForeignKey(menshirts,on_delete=models.CASCADE)
        order = models.ForeignKey(Order ,on_delete=models.CASCADE)
        price=models.DecimalField(max_digits=6, decimal_places=2)
        quantity=models.IntegerField()

        def __str__(self):
            return 'User: ' + self.order.user.username + ',product: ' + self.product.name + ',Order id: ' +str(self.order.id)




