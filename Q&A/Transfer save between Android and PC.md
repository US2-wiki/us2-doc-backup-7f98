1. Export your android save
2. Copy the save file from Android 
	   Path: ``/storage/emulated/0/Android/data/com.enigmadev.uploadsimulator2/files`` 
	   If you unable to find the path, you can use USB debug with adb to retrieve the save file:
	```
	cd storage/emulated/0
	cp Android/data/com.enigmadev.uploadsimulator2/files/savegame.save savegame.save
	```
	 And you can find the save file in `/storage/emulated/0`
3. Paste to PC ``%appdata%\Godot\app_userdata\Upload Simulator 2`` with filename `savegame.save`