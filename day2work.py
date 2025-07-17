{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "927b632b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#billing management system"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5362c83e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the product namemaggi\n",
      "enter the price200\n",
      "enter its quatity10\n",
      "total price of all product and its quatity is \n",
      "2000\n"
     ]
    }
   ],
   "source": [
    "product=str(input(\"enter the product name\"))\n",
    "price=int(input(\"enter the price\"))\n",
    "quantity=int(input(\"enter its quatity\"))\n",
    "sum=price*quantity\n",
    "print(\"total price of all product and its quatity is \")\n",
    "print(sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "25487393",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the namevivek\n",
      "enter the age18\n",
      "eligible to vote\n"
     ]
    }
   ],
   "source": [
    "#vote\n",
    "name=str(input(\"enter the name\"))\n",
    "age=int(input(\"enter the age\"))\n",
    "if age>=18:\n",
    "    print(\"eligible to vote\")\n",
    "else:\n",
    "    print(\"not eligible to vote\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0ffe8f79",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the no -1\n",
      "negative\n"
     ]
    }
   ],
   "source": [
    "#positive or not\n",
    "a=int(input(\"enter the no \"))\n",
    "if a>0:\n",
    "    print(\"positive\")\n",
    "else:\n",
    "    print(\"negative\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a84e1946",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the age18\n",
      "eligible\n"
     ]
    }
   ],
   "source": [
    "#vote\n",
    "age=int(input(\"enter the age\"))\n",
    "if age>=18:\n",
    "    print(\"eligible\")\n",
    "else:\n",
    "    print(\"not eligible\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "b887ffa9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the no 0\n",
      "whole no\n"
     ]
    }
   ],
   "source": [
    "#even or odd\n",
    "a=int(input(\"enter the no \"))\n",
    "if a==0:\n",
    "    print(\"whole no\")\n",
    "elif a%2==0:\n",
    "    print(\"even\")\n",
    "else:\n",
    "    print(\"odd\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "c61940bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the nameabhimaniyu\n",
      "the length is greater than 5\n"
     ]
    }
   ],
   "source": [
    "#length check\n",
    "name=str(input(\"enter the name\"))\n",
    "if len(name)>5:\n",
    "    print(\"the length is greater than 5\")\n",
    "else:\n",
    "    print(\"it is not\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "c2020029",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the marks 50\n",
      "pass\n"
     ]
    }
   ],
   "source": [
    "#pass or fail\n",
    "marks=int(input(\"enter the marks \"))\n",
    "if marks>=40:\n",
    "    print(\"pass\")\n",
    "else:\n",
    "    print(\"fail\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fdfe428c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the monthoctober\n",
      "spring\n"
     ]
    }
   ],
   "source": [
    "#weather check\n",
    "month=str(input(\"enter the month\"))\n",
    "if month in ['December','january','febaury']:\n",
    "    print(\"winter\")\n",
    "elif month in['June','july','august']:\n",
    "    print(\"summer\")\n",
    "elif month in['marth','april','may']:\n",
    "    print(\"autumn\")\n",
    "elif month in['september','october','november']:\n",
    "    print(\"spring\")\n",
    "else:\n",
    "    print(\"invalid month\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "207a2cff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter mode of transportwater\n",
      "enter vehicleship\n",
      "you are in ship\n"
     ]
    }
   ],
   "source": [
    "#check mode of transport\n",
    "modeoftransport=str(input(\"enter mode of transport\"))\n",
    "vehicle=str(input(\"enter vehicle\"))\n",
    "if modeoftransport==\"air\":\n",
    "    if vehicle==\"aeroplane\":\n",
    "        print(\"you are in aeroplane\")\n",
    "    elif vehicle==\"helicopter\":\n",
    "        print(\"you are in helicopter\")\n",
    "if modeoftransport==\"water\":\n",
    "    if vehicle==\"ship\":\n",
    "        print(\"you are in ship\")\n",
    "    elif vehicle==\"cruise\":\n",
    "        print(\"you are in cruise\")\n",
    "if modeoftransport==\"land\":\n",
    "    if vehicle==\"car\":\n",
    "        print(\"you are in car\")\n",
    "    elif vehicle==\"bus\":\n",
    "        print(\"you are in bus\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9e2723fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the no. 0\n",
      "zero\n"
     ]
    }
   ],
   "source": [
    "#positive or negative or zero\n",
    "num=int(input(\"enter the no. \"))\n",
    "if num>0:\n",
    "    print(\"positive\")\n",
    "elif num<0:\n",
    "    print(\"negative\")\n",
    "else:\n",
    "    print(\"zero\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "abe6c10c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the age :18\n",
      "adult\n"
     ]
    }
   ],
   "source": [
    "#child or teen or adult\n",
    "age=int(input(\"enter the age :\"))\n",
    "if age<13:\n",
    "    print(\"child\")\n",
    "elif age<18:\n",
    "    print(\"teen\")\n",
    "else:\n",
    "    print(\"adult\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "765598ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the no. 12\n",
      "even\n",
      "num greater than 10\n"
     ]
    }
   ],
   "source": [
    "#even or not (nested if)\n",
    "num=int(input(\"enter the no. \"))\n",
    "if num%2==0:\n",
    "    print(\"even\")\n",
    "    if num>10:\n",
    "        print(\"num greater than 10\")\n",
    "    else:\n",
    "        print(\"it is not \")\n",
    "else:\n",
    "    print(\"odd\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8c5ddb16",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the marks 80\n",
      "B\n"
     ]
    }
   ],
   "source": [
    "#grade check\n",
    "marks=int(input(\"enter the marks \"))\n",
    "if marks>90:\n",
    "    print(\"A\")\n",
    "elif marks>75:\n",
    "    print(\"B\")\n",
    "elif marks>60:\n",
    "    print(\"C\")\n",
    "else:\n",
    "    print(\"fail\")    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "fb114456",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the no2\n",
      "enter 2nd no10\n",
      "enter 3rd no100\n",
      "c is greater \n"
     ]
    }
   ],
   "source": [
    "#largest no (nested if)\n",
    "a=int(input(\"enter the no\"))\n",
    "b=int(input(\"enter 2nd no\"))\n",
    "c=int(input(\"enter 3rd no\"))\n",
    "if a>b:\n",
    "    if a>c:\n",
    "        print(\"a is greater\")\n",
    "    else:\n",
    "        print(\"c is greater\")\n",
    "        \n",
    "else:\n",
    "    if b>c:\n",
    "        print(\"b is greater\")\n",
    "    else:\n",
    "        print(\"c is greater \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8d5507d6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "table of 2\n",
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n",
      "12\n",
      "14\n",
      "16\n",
      "18\n",
      "20\n",
      "table of 3\n",
      "3\n",
      "6\n",
      "9\n",
      "12\n",
      "15\n",
      "18\n",
      "21\n",
      "24\n",
      "27\n",
      "30\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# 2 tables using while loop\n",
    "i=1 \n",
    "print(\"table of 2\")\n",
    "while i<=10:\n",
    "    print(2*i)\n",
    "    i+=1\n",
    "j=1\n",
    "print(\"table of 3\")\n",
    "while j<=10:\n",
    "    print(3*j)\n",
    "    j+=1\n",
    "print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74057581",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "44e432d1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
