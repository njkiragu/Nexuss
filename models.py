from django.db import models
from django.contrib.auth.models import User
import hashlib as hl
import datetime as dt

# This class is used to save each chain in the database separately.
class Chain(models.Model):
    """
    This model class enables us to save each blockchain separately per user in the database.
    """
    name = models.CharField(max_length=255, default = 'null')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.IntegerField(default = 'null')
    sem = models.CharField(max_length=30,default = 'null')
    code = models.CharField(max_length=10,default = 'null')
    slot = models.CharField(max_length=10,default = 'null')
    strength = models.CharField(max_length = 255, default = 'null')
    last_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

# This class is used to save each block in the database separately.
class Block(models.Model):
    """
    This model class enables us to save each block in the database.
    """
    index = models.IntegerField(null=True)
    chain = models.ForeignKey(Chain, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.TextField()
    prev_hash = models.CharField(max_length=500)

    def __str__(self):
        return "Block #" + str(self.index) + " on " + self.chain.name

# This function is used to store the hash of the block as a property that
# is automatically calculated everytime a block is generated or modified.
    @property
    def block_hash(self):
        sha = hl.sha256()
        sha.update(str(self.index).encode() + str(self.timestamp).encode() + str(self.data).encode() + str(self.prev_hash).encode())
        return sha.hexdigest()
    