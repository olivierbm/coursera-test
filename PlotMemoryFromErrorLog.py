import re

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt

handlefile = open(r'D:\python\S3DError_2016_06_10_22_53_16.log')
listofElapsedTime =  list()
listOfLargestFreeBlock = list()
listOfCommitMemory = list()
listofReservedMemory = list()
for line in handlefile:
    if re.search('^OS', line):
        listofelapsed = re.findall('elapsed,([^,]*)', line)
        ListOfLargetFree = re.findall('largest free,([^,]*)', line)
	ListOfCommit = re.findall('commit,([^,]*)', line)
        listofReserved = re.findall('reserved,([^,]*)', line)
        if len(listofelapsed) > 0:
            listofElapsedTime.append(listofelapsed)
        if len(ListOfLargetFree) > 0:
            listOfLargestFreeBlock.append(ListOfLargetFree)
        if len(ListOfCommit) > 0:
            listOfCommitMemory.append(ListOfCommit)
        if len(listofReserved) > 0:
            listofReservedMemory.append(listofReserved)
print(len(listOfLargestFreeBlock))


if 1:

    host = host_subplot(111, axes_class=AA.Axes)
    plt.subplots_adjust(right=0.75)

    par1 = host.twinx()
    par2 = host.twinx()

    offset = 60
    new_fixed_axis = par2.get_grid_helper().new_fixed_axis
    par2.axis["right"] = new_fixed_axis(loc="right",
                                        axes=par2,
                                        offset=(offset, 0))

    par2.axis["right"].toggle(all=True)

    print(max(listofElapsedTime))
    print(max(listOfLargestFreeBlock))

    host.set_xlim(0, 2850)
    host.set_ylim(0, 3000)

    host.set_xlabel("Elapsed Time")
    host.set_ylabel("Memory Largest Free block (MB)")
    par1.set_ylabel("Memory Commit (MB)")
    par2.set_ylabel("memory reserved (MB)")

    p1, = host.plot(listofElapsedTime, listOfLargestFreeBlock, label="Free")
    p2, = par1.plot(listofElapsedTime, listOfCommitMemory, label="Commit")
    p3, = par2.plot(listofElapsedTime, listofReservedMemory, label="Reserved")

    par1.set_ylim(0, 3000)
    par2.set_ylim(0, 3000)

    host.legend()

    host.axis["left"].label.set_color(p1.get_color())
    par1.axis["right"].label.set_color(p2.get_color())
    par2.axis["right"].label.set_color(p3.get_color())

    plt.draw()
    plt.show()
