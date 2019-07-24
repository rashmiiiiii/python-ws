def appointment(**kwargs):
    did =kwargs['did']
    uid = kwargs['uid']
    day = kwargs['day']
    print(f"did:{did} and uid:{uid} day:{day}")

appointment(did=1001,uid=9001,day=22,time=22,year=2019,isActive = False)  