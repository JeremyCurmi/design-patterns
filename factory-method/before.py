from abc import ABC, abstractmethod

class TransportMethods:
    TRUCK = "truck"
    MOTORBIKE = "motorbike"


class TransportService(ABC):
    @abstractmethod
    def prepare_shipment(self):
        pass

    @abstractmethod
    def send_shipment(self):
        pass

class TruckTransportService(TransportService):
    def prepare_shipment(self):
        print("Loading shipment on truck")

    def send_shipment(self):
        print("Shipment is on the way on a truck")

class MotorbikeTransportService(TransportService):
    def prepare_shipment(self):
        print("Loading shipment on motorbike")

    def send_shipment(self):
        print("Shipment is on the way on a motorbike")


if __name__ == '__main__':
    """main function"""
    Transport: TransportService

    while True:
        transport_method = input("Choose preferred shipping method, available options: ['truck', 'motorbike'] ")
        if transport_method in ["truck", "motorbike"]:
            break
        print("This is not offered yet, please choose another method")


    if transport_method == TransportMethods.TRUCK:
        transport = TruckTransportService()
    elif transport_method == TransportMethods.MOTORBIKE:
        transport = MotorbikeTransportService()

    transport.prepare_shipment()
    transport.send_shipment()