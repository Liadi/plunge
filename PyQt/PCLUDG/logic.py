__author__ = 'Omotola'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from enum import Enum
from math import floor
from  math import pow
import sys
import customInterfaceWidget

class Region(Enum):
    Void = 0
    NorthWest = 1
    NorthEast = 2
    SouthEast = 3
    SouthWest = 4

class Decision():
    def __init__(self):
        pass
    def main(self, source = -1, target = -1, constant = -1):
        if source == -1 or target == -1:
            return [False,-1]
        sourceRow, sourceColumn = source.getMatrix()
        targetRow, targetColumn = target.getMatrix()
        if constant >= 0 and constant <= 49:
            constantRow, constantColumn = constant.getMatrix()
            if constant != source:
                return [False,self.getTileIndex(constantRow, constantColumn)]
            else:
                pass
        if target.getStatus() != customInterfaceWidget.Status.void:
            return [False,-1]

        if pow(targetRow - sourceRow, 2) == 4 and pow(targetColumn - sourceColumn, 2) == 4:#if diff of source and target is two(i.e jumps over 1 tile)
            i = (targetRow - sourceRow)/2 + sourceRow#row of tile in between
            j = (targetColumn - sourceColumn)/2 + sourceColumn#column of tile in between
            index = int(i * 5 + floor(j/2))#index of jumped tile
            if 2/source.getStatus().value == customInterfaceWidget.Board.tileArray[index].getStatus().value:
                customInterfaceWidget.Board.tileArray[index].setStatus(customInterfaceWidget.Status.void)
                customInterfaceWidget.Board.tileArray[index].setIcon(QIcon(QPixmap("")))
                target.setIcon(source.getIcon())
                source.setIcon(QIcon(QPixmap("")))
                tempStatus = target.getStatus()
                tempState = target.getState()
                target.setStatus(source.getStatus())
                target.setState(source.getState())
                source.setStatus(tempStatus)
                source.setState(tempState)

                if self.decider(self.getTileIndex(targetRow, targetColumn))[1]:
                    return [True, self.getTileIndex(targetRow, targetColumn)]

                else:
                    return [True,-1]

            else:
                return [False, -1]


        elif (source.getStatus().value == 2 and targetRow - sourceRow == 1 and pow(targetColumn - sourceColumn,2) == 1)\
                or (source.getStatus().value == 1 and targetRow - sourceRow == -1 and pow(targetColumn - sourceColumn, 2) == 1):#if diff of source and target is one(i.e moves to an adjacent)

            returnValue = [True, -1]
            for i in range(0,50,1):
                region, bol = self.decider(i)
                if bol:
                    returnValue = [False, -1]
                else:
                    continue

            if returnValue[0]:
                target.setIcon(source.getIcon())
                target.setStatus(source.getStatus())
                source.setIcon(QIcon(QPixmap("")))
                source.setStatus(customInterfaceWidget.Status.void)
            return returnValue

        return [False,-1]

    def getTileIndex(self, row, col):#return tile obj with row "row" and column "col"
        return row*5 + floor(col/2)

    def decider(self,i):#checks if there is a possible jump that should be enforced
        board = customInterfaceWidget.Board
        source = board.tileArray[i]
        region = []
        bol = False
        returnValue = [region, bol]
        if board.tileArray[i].getState() == customInterfaceWidget.State.live:
            row, col = source.getMatrix()

            try:
                if row - 2 < 0 or col - 2 < 0 or row - 2 > 9 or col - 2 > 9:
                    raise IndexError("array out of bound")
                else:
                    if (board.tileArray[self.getTileIndex(row - 1, col - 1)].getStatus().value == int(2/source.getStatus().value) and board.tileArray[self.getTileIndex(row - 2, col - 2)].getStatus().value == 0):
                        region.append(Region.NorthWest.value)
                        bol = True
                        returnValue = [region, bol]
            except IndexError as err:
                pass


            #North East
            try:
                if row - 2 < 0 or col + 2 < 0 or row - 2 > 9 or col + 2 > 9:
                    raise IndexError("array out of bound")
                else:
                    if (board.tileArray[self.getTileIndex(row - 1, col + 1)].getStatus().value == 2/source.getStatus().value and board.tileArray[self.getTileIndex(row - 2, col + 2)].getStatus().value == 0):
                        region.append(Region.NorthWest.value)
                        bol = True
                        returnValue = [region, bol]
            except IndexError as err:
                pass


            #South East
            try:
                if row + 2 < 0 or col + 2 < 0 or row + 2 > 9 or col + 2 > 9:
                    raise IndexError("array out of bound")
                else:
                    if (board.tileArray[self.getTileIndex(row + 1, col + 1)].getStatus().value == 2/source.getStatus().value and board.tileArray[self.getTileIndex(row + 2, col + 2)].getStatus().value == 0):
                        region.append(Region.NorthWest.value)
                        bol = True
                        returnValue = [region, bol]
            except IndexError as err:
                pass

            #South West
            try:
                if row + 2 < 0 or col - 2 < 0 or row + 2 > 9 or col - 2 > 9:
                    raise IndexError("array out of bound")
                else:
                    if (board.tileArray[self.getTileIndex(row + 1, col - 1)].getStatus().value == 2/source.getStatus().value and board.tileArray[self.getTileIndex(row + 2, col - 2)].getStatus().value == 0):
                        region.append(Region.NorthWest.value)
                        bol = True
                        returnValue = [region, bol]
            except IndexError as err:
                pass


        return returnValue

    def control(self, sideEnum):

        if sideEnum == customInterfaceWidget.Side.A:
            for i in range(0,50,1):

                if customInterfaceWidget.Board.tileArray[i].getStatus().value == 1:
                    customInterfaceWidget.Board.tileArray[i].setState(customInterfaceWidget.State.live)
                else:
                    customInterfaceWidget.Board.tileArray[i].setState(customInterfaceWidget.State.dead)

        elif sideEnum == customInterfaceWidget.Side.B:
            for i in range(0,50,1):
                if customInterfaceWidget.Board.tileArray[i].getStatus().value == 2:
                    customInterfaceWidget.Board.tileArray[i].setState(customInterfaceWidget.State.live)
                else:
                    customInterfaceWidget.Board.tileArray[i].setState(customInterfaceWidget.State.dead)  # to be inherited!!!


