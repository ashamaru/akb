
import time

from .models import *
from django.db.models import Max
from django.core.exceptions import ObjectDoesNotExist


# Here the auction logic in reference to the database is implemented

class Delegate(object):
    lock = None
    res = None
    # necessary for data inconsitency
    def lock(self):
        waiting = True
        while waiting is True:
                try:
                    self.lock = DelegateLock.objects.get(d_id=1)
                except DelegateLock.DoesNotExist:
                    waiting = False
                self.lock = None
                time.sleep(0.2)
                print('Waiting for lock')

        if self.lock is None:
            self.lock = DelegateLock(d_id = 1)
            self.lock.d_lockval = 1
            self.lock.save()
        else:
           raise Exception('KyoDelegateLockException')

    # releases the request and lets others bid
    def unlock(self):
        self.lock.delete()

    def processBid(self, bid):
        self.lock()
        print('Validating bid')
        print('Bid { ' + bid.b_article.a_name + ' of ' + str(bid.b_amount))
        try:
            self.validateBid(bid)
        finally:
            self.unlock()

    # Revalidating the bid
    def validateBid(self, bid):
        mobj = Bid.objects.all().filter(b_article__a_id = bid.b_article.a_id).aggregate(Max('b_amount'))
        print(str(mobj))
        print('Is amaout higher than the berfore')
        if mobj['b_amount__max'] is None or bid.b_amount > mobj['b_amount__max']:
            self.res = 'Valid'
            print('saving the new bid')
            bid.save()
        else:
            print('bid was invalid')
            self.res = 'Failure'

