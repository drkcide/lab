class Account:
    """
    A class to establish ownership and balance of an account
    """

    def __init__(self, name: str) -> None:

        """
        Constructor to create initial state of account
        :param name: Name of account holder
        """

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Method to deposit money into account holder's account using
        exception handling and if/else statement
        :param amount: amount to be deposited
        :return: boolean statement if transaction was successful
        """
        try:
            if amount > 0:
                self.__account_balance += amount
                return True
            else:
                return False
        except TypeError:
            return False

    def withdraw(self, amount: float) -> bool:
        """Method to withdraw money from account holder's account using
        exception handling and if/else statements
        :param amount:
        :return: boolean statement if transaction was successful
        """
        try:

            if amount <= 0 or amount > self.__account_balance:
                return False
            else:
                self.__account_balance -= amount
                return True
        except TypeError:
            return False

    def get_balance(self) -> float:
        """
        Method to access account balance
        :return: the current account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to access account holder's name
        :return: account holder's name
        """
        return self.__account_name
