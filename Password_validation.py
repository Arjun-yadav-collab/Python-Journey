{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6f88355f-7a81-4118-8bd5-a97de459c9b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a password to validate:  Arjun@123\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Password is valid!\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "def valid_password(password):\n",
    "    if len(password) <8:\n",
    "        return \"Password must be at least 8 characters long.\"\n",
    "    \n",
    "    if not re.search(r\"[A-Z]\", password):\n",
    "        return \"Password must contain at least one uppercase letter.\"\n",
    "    \n",
    "    if not re.search(r\"[a-z]\", password):\n",
    "        return \"Password must contain at least one lowercase letter.\"\n",
    "    \n",
    "    if not re.search(r\"[0-9]\", password):\n",
    "        return \"Password must contain at least one digit.\"\n",
    "    \n",
    "    if not re.search(r\"[!@#$%^&*(),.?\\\":{}|<>]\", password):\n",
    "        return \"Password must contain at least one special character.\"\n",
    "    \n",
    "    return \"Password is valid!\"\n",
    "\n",
    "password_input = input(\"Enter a password to validate: \")\n",
    "validation_result = valid_password(password_input)\n",
    "print(validation_result)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "047a1f2c-a127-424f-9ee0-d7c3f134218c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
