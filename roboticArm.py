
# this is a class for a robotic arm that stores the lengths of its sections and the location and the angles of each of
# its join and can recalculate the location of each joint even if the angles were changed

class roboticArm:
    # initialises the robotic arm with the appropriate length and default angles to make an an arm that is vertically
    # stretched perpendicular to ground

    def __init__(self, lengths):  # constructor only takes the lengths of the sections of arm
        self.lengths = []  # stores length of each section of arm
        self.lengths = lengths  # assigning the inputed length to the arm
        self.angles = []  # stores value of angles of joints between sections of arms
        self.trueAngles = []  # stores value of angle at each join in relation to ground
        self.coordinates = []  # stores x and y coordinates of each joint of arm
        self.angles.append(math.pi / 2)  # initialises he first section of arm to be perpendicular to ground
        self.coordinates.append(point(0, self.lengths[0]))  # initializes the location of the first section of arm
        # initializes the angle of all he joints such that the ar is a straight one perpendicular
        # to ground and temporarily sets the coordinated based on the length of the sections of the arms without the
        # consideration that they are connected, but wil be fixed by the next loop
        for i in range(1, len(self.lengths)):
            self.angles.append(math.pi)
            self.coordinates.append(point(0, self.lengths[i]))
        # corrects the coordinates of each joint to arrive at the correct coordinates for each joint
        for i in range(1, len(self.lengths)):
            self.coordinates[i] = point(self.coordinates[i].x + self.coordinates[i - 1].x,
                                        self.coordinates[i].y + self.coordinates[i - 1].y)

    # method to change the angles of the robotic arm and recalculate the position of each joint
    def setAngles(self, angles):  # method accepts the values of the new angles
        self.angles = angles  # changes the stored value of angles
        # calculates the true angles relative to ground from the angles using the parallel line angle theorems
        self.trueAngles.append(self.angles[0])
        for i in range(1, len(self.lengths)):
            self.trueAngles.append(self.angles[i] - (math.pi - self.angles[i - 1]))
        # declares lists to store the horizontal run and vertical rise of each section of arm
        self.rawDeltaX = []
        self.rawDeltaY = []
        # calculates the rise and run of each arm
        for i in range(0, len(self.lengths)):
            self.rawDeltaX.append(math.cos(self.trueAngles[i]))
            self.rawDeltaY.append(math.sin(self.trueAngles[i]))
        # temporarily recalculates the coordinates for each point without considering the fact that they are all linked
        for i in range(0, len(self.lengths)):
            self.coordinates[i] = point(self.rawDeltaX[i] * self.lengths[i], self.rawDeltaY[i] * self.lengths[i])
        # corrects for the fact that the sections are linked and stores the true values of the coordinates of the joints
        for i in range(1, len(self.lengths)):
            self.coordinates[i] = point(self.coordinates[i].x + self.coordinates[i - 1].x,
                                        self.coordinates[i].y + self.coordinates[i - 1].y)


# point class to store x and y coordinate of each joint
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

