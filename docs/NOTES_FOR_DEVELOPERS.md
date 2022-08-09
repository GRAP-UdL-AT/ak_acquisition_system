# AK_ACQS - Notes for developers

## 1. Hierarchy folder

In this work, we proposed a hierarchy folder as following.

```
|---/$HOME
	|---/development
		|---/ak_acquisition_system-main
			|---/remote_client_ak
			|---/remote_client_generic
			|---/remote_client_zed
			|---/remote_management_console
			|---/server_rest_api

	|---/development_env
		|---/ak_acquisition_system-main_venv
			|---/remote_client_ak_venv
			|---/remote_client_generic_venv
			|---/remote_client_zed_venv
			|---/remote_management_console_venv
			|---/server_rest_api_venv
```

Automatic scripts were developed to facilitate work for developers.

## 2. Demos

### 2.1 Demo - AK_ACQS components working together

This video shows how the components can interact with each other using the remote management console. Represents a
sequence about the components of AK_ACQS that work together: Server Rest API, Remote Management Console, Remote Client
Generic.
![server_video_demo_01](https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/docs/img/server_demo_usage_01.gif?raw=true)

### 2.2 Demo - AK_ACQS components and Azure Kinect remote client

This video shows how the components can interact with each other using the remote management console, especially showing
Azure Kinect remote client activations.

![server_video_demo_02](https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/docs/img/server_demo_usage_02.gif?raw=true)
