from django.db import models

class Value(models.Model):
   moringa_value = models.CharField(max_length=200)
   emp= models.ManyToOneRel(moringa_value,'Employee.name','emp')
   class Meta:
      ordering = ('moringa_value',)

   def __str__(self):
      
      # employees = self.moringa_value.all()
      
      return f'{self.moringa_value}'
class Employee(models.Model):
   name = models.CharField(max_length=200)
   moringa_values = models.ManyToManyField(Value,related_name='val',related_query_name='qval', blank = True)
   
   votes = models.PositiveIntegerField(default=0)

   class Meta:
      ordering = ('name',)

   def __str__(self):
      count = self.moringa_values.count()
      
      # for val in values:
      #    print(self.name ,val)
      #    pass
      return f'{self.name}, has {count} values!'

   # @classmethod
   # def cal_votes(self):
   #    mo_val = self.moringa_values.all()
   #    print(mo_val)
   #    values = Value.objects.filter(moringa_value='moringa_value')
   #    for i in mo_val:
   #       if i in values:
   #          @property
   #          def add_v():
   #             votes = self.votes
   #             votes+=1
   #             return votes.save()
   #          return add_v()
   # cal_votes('Employee')
