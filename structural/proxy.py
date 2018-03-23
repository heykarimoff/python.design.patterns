import time


class Producer:
    """Define 'resource-intensive' object to instantiate"""

    def produce(self):
        print('Producer is working hard!')

    def meet(self):
        print('Producer has time to meet you now!')


class Proxy:
    """Define relatively less 'resource-intensive' proxy to instantiate as a middleman"""

    def __init__(self):
        self.is_occupied = False
        self.producer = None

    def produce(self):
        """Check if Producer is available"""
        print('Artist cheking if producer is available ...')

        if not self.is_occupied:
            self.producer = Producer()
            time.sleep(3)

            self.producer.meet()
        else:
            print('Producer is busy!')


proxy = Proxy()
proxy.produce()

proxy.is_occupied = True
proxy.produce()
