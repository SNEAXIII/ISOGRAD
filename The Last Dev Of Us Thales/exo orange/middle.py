import sys, io

sampleToTest = "11"
with open(f"dataSample/output{sampleToTest}.txt") as f:
    outputExpected = int(f.read())
with open(f"dataSample/input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())


# START
def convertHourMinuteToMinute(stringHourMinute):
    hour,minute = map(int,stringHourMinute.split(":"))
    return hour * 60 + minute


numberOfSurvivor = int(input())

# Get all survivors in the format "[[100,200],[300,400],[500,600]]"
listAllSurvivor = [list(map(convertHourMinuteToMinute, input().split(" - "))) for _ in range(numberOfSurvivor)]

# Sorted by order of arrival at the common room
listAllSurvivor.sort(key=lambda x: x[0])

numberOfRisk = 0
listInCommonRoom = []

for incomingSurvivor in listAllSurvivor:
    leavingSurvivor = []
    # We select the arrival and departure times of the incoming survivor
    minuteStartIncoming, minuteStopIncoming = incomingSurvivor

    for index, selectedSurvivorInRoom in enumerate(listInCommonRoom):
        minuteStopLeaving = selectedSurvivorInRoom[1]

        # If a new survivor joins the common room after an
        # occupant has left, he must be removed from the room.
        if minuteStopLeaving < minuteStartIncoming:
            leavingSurvivor.append(index)

        # If a new survivor is in contact with the same survivor
        # for 15 minutes or more, an alert is triggered.
        elif min(minuteStopLeaving, minuteStopIncoming) - minuteStartIncoming >= 15:
            numberOfRisk += 1

    # Delete all survivors no longer in the room
    for idPersonne in leavingSurvivor[::-1]:
        del listInCommonRoom[idPersonne]

    # The new survivor joins common room
    listInCommonRoom.append(incomingSurvivor)

print(numberOfRisk)
# END

if outputExpected == numberOfRisk:
    print("Le test est valide")
else:
    print(f"Le test n'est pas valide --> output = {numberOfRisk} contre exepct = {outputExpected}")
