# Protocol example -->  IP:COLOR:DATATYPE:DATA:DATATYPE:DATA


def is_on_table(search_ip, robot_info):
    for idx, elem in enumerate(robot_info):
        if elem.ip == search_ip:
            return True, idx
    return False, None


class Protocol:
    """
    Docstring for robotInfo.
    """

    def __init__(self, ip="8.8.8.8", color="BLACK"):
        self.ip = ip
        self.color = color

        self.pos_x = 0.0
        self.pos_y = 0.0

        self.state = "WAIT_CONN"
        self.message = ''

        self.prepared_message = ''


    def __str__(self):
        return "IP:{0:17} | " \
               "COLOR:{1:10} | " \
               "STATE:{2:10} | " \
               "MSG:{3:10}".format(self.ip,
                                   self.color,
                                   self.state,
                                   self.message)

    def build_data(self):
        built_data = self.ip + ":" + \
                     self.color + ":" + \
                     "STATE:" + self.state + ":" + \
                     "POSX:" + str(self.pos_x) + ":" + \
                     "POSY:" + str(self.pos_y) + ":" + \
                     "MSG:" + self.message

        self.prepared_message = built_data
        return built_data

    @staticmethod
    def decode_data(self, data):
        """
        TODO: add exceptions

        :param data: message from robots
        :return: ip, color, other data
        """

        data = data.split(":")

        ip = data[0]
        color = data[1]

        data = data[2::] # data without IP and COLOR

        # Create list of tuples (DATATYPE, DATA)
        data_list = list(zip(data[0::2], data[1::2]))

        return ip, color, data_list

    def save_data(self, data):
        ip, color, data_list = self.decode_data(data)

        self.set_ip(ip)
        self.set_color(color)

        for data_type, data_value in data_list:
            if data_type == "POSX":
                self.set_pos_x(float(data_value))
            elif data_type == "POSY":
                self.set_pos_y(float(data_value))
            elif data_type == "STATE":
                self.set_state(data_value)
            elif data_type == "MSG":
                self.set_message(data_value)
            else:
                print("Protocol Error")
                return False
        return True

    def set_ip(self, ip="8.8.8.8"):
        self.ip = ip

    def set_color(self, color="BLACK"):
        self.color = color

    def set_state(self, state="ALIVE"):
        self.state = state

    def set_message(self, message="HELLO"):
        self.message = message

    def set_pos_x(self, pos=0.0):
        self.pos_x = pos

    def set_pos_y(self, pos=0.0):
        self.pos_y = pos
