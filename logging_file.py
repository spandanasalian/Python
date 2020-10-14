# import logging 
# print(dir(logging))

# import logging 
# logging.basicConfig(filename="C:\\Users\\spandana\\Desktop\\python file\\ul.log",level=logging.DEBUG)
# logger=logging.getLogger()

# logger.info("Servers are running fine.")
# logger.debug("Servers are running fine(2).")
# logger.warning("Servers are running fine(@).")



# import logging 
# logging.basicConfig(filename="C:\\Users\\spandana\\Desktop\\python file\\ul.log",
#                     level=logging.DEBUG,
#                     filemode='w')
# logger=logging.getLogger()

# # logger.info("Servers are running fine.")
# logger.debug("Servers are running fine(2).")
# # logger.warning("Servers are running fine(@).")

# import logging 
# logging.basicConfig(filename="test.log",
#                     level=logging.DEBUG,
#                     filemode='w')
# logger=logging.getLogger()

# logger.info("Servers are running fine.")
# logger.debug("Servers are running debug fine.")
# logger.warning("Servers are running warning fine(@).")
# logger.error("Servers are running error fine.")
# logger.critical("Servers are running critical fine(@).")

import logging 
LOG_FORMATE="%(levelname) s%(asctime)s-%(message)s"
logging.basicConfig(filename="test.log",
                     level=logging.ERROR,
                     filemode='w',
                     format=LOG_FORMATE)
logger=logging.getLogger()

logger.info("Servers are running fine.")
logger.debug("Servers are running debug fine.")
logger.warning("Servers are running warning fine(@).")
logger.error("Servers are running error fine.")
logger.critical("Servers are running critical fine(@).")





