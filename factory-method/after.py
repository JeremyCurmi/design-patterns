from abc import ABC, abstractmethod

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

class TransportFactory(ABC):
    def create_transport(self) -> TransportService:
        """returns a new transport object"""

class TruckFactory(TransportFactory):
    """Factory aimed at providing truck service"""
    def create_transport(self) -> TransportService:
        return TruckTransportService()


class MotorbikeFactory(TransportFactory):
    """Factory aimed at providing truck service"""
    def create_transport(self) -> TransportService:
        return MotorbikeTransportService()

def read_transport_method() -> TransportFactory:
    """Creates the Transport Factory"""
    if __name__ == '__main__':
        factories = {
            "truck": TruckFactory(),
            "motorbike": MotorbikeFactory(),
        }

        while True:
            transport_method = input("Choose preferred shipping method, available options: ['truck', 'motorbike'] ")
            if transport_method in factories:
                return factories[transport_method]

def main(factory: TransportFactory):
    """Using the Transport Factory"""
    transport_service = transport_factory.create_transport()
    transport_service.prepare_shipment()
    transport_service.send_shipment()

# Notice that we seperated creation and use of the transport service!

if __name__ == '__main__':
    transport_factory = read_transport_method()
    main(transport_factory)
