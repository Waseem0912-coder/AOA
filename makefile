# Define Python interpreter
PYTHON := python3

# Phony targets for non-file commands
.PHONY: all clean run1 run2a run2b run3 run4 run5 run6a run6b run7 run8

# Default target
all:
	@echo "All tasks are up to date."

# Rules for running tasks
run1:
	@$(PYTHON) task1.py

run2A:
	@$(PYTHON) task2A.py

run2B:
	@$(PYTHON) task2B.py

run3:
	@$(PYTHON) task3.py

run4:
	@$(PYTHON) task4.py

run5:
	@$(PYTHON) task5.py

run6A:
	@$(PYTHON) task6A.py

run6B:
	@$(PYTHON) task6B.py

run7:
	@$(PYTHON) task7.py

run8:
	@$(PYTHON) task8.py

# Clean up command (optional, based on your needs)
clean:
	@echo "Cleaning up..."
	# Add your clean-up commands here (like removing temporary files)

# Other custom commands (if any) can go here
