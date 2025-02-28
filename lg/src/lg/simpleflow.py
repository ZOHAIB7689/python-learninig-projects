from langgraph.func import entrypoint, task
import time

@task
def task1():
    print("Task 1 ")
    return "Task 1 Executed"

@task()
def task2():
    print("Task 2")
    return "Task 2 Executed"
    


@entrypoint()
def run_flow(input:str):
    print("Running Simple Workflow", input)
    task1_output = task1()
    task2_output = task2()
    return f"workflow executed successfully with outputs {task1_output} and {task2_output}"


def  run_chain():
    run_flow.invoke("Simple Input")



def check_entrypoint(func):
    def wraper(input):
        print("Checking Entry Point")
        return func(input)
    return wraper