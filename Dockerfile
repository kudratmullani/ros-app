FROM ros:jazzy-ros-base

SHELL ["/bin/bash", "-c"]

# Create app directory
WORKDIR /app

# Copy only the Python node
COPY ros2_ws/src/demo_pkg/demo_pkg/talker.py ./talker.py

# Run the node directly
CMD ["bash", "-c", "source /opt/ros/jazzy/setup.bash && python3 /app/talker.py"]

