from crewai.flow.flow import Flow, start,listen
import time

class SimpleFlow(Flow):
    

    @start()
    def func1(self):
        print("step1...")
        time.sleep(2)
    
    @listen(func1)
    def func2(self):
        print("step2...")
        time.sleep(2)



    @listen(func2)
    def func3(self):
        print("step3....")
        time.sleep(2)

def kickoff():
    obj = SimpleFlow()
    obj.kickoff()