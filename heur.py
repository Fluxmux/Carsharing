class Request:
    def __init__(self, id, zone,dag,start,duur,vehicles,p1,p2):
        self.id=id
        self.zone=zone
        self.dag=dag
        self.start=start
        self.duur=duur
        self.vehicles=vehicles
        self.p1=p2
        self.p2=p2
class Zone:
    def __init__(self,id,near):
        self.id=id
        self.near=near
