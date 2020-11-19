# Job: A process or task that has a priority.
# Your implementation should pass the tests in test_job.py.
# Nick Morris

class Job:

    def __init__(self, priority = None, message = None):
        self.priority = priority
        self.message = message

    def __eq__(self, comp):
        return self.priority == comp.priority

    def __lt__(self, comp):
        return self.priority < comp.priority

    def __gt__(self, comp):
        return self.priority > comp.priority
    
    def __le__(self, comp):
        return self.priority <= comp.priority

    def __ge__(self, comp):
        return self.priority >= comp.priority
    
    def __repr__(self):
        return "Job %s: %s" % (self.priority, self.message)