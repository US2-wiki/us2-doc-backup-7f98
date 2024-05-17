---
tags:
  - Main
aliases:
  - file
  - filetype
---
There are a few different file type in the game:
- [[Image]]
- [[Music]]
- [[Video]]
- [[Game]]
- [[Requests]]
- [[Drivers]] (Require [[Drivers (Research)]] technologies research at [[Tier 2]] with $1e12$ [[Science B]])

## How to get the file?
- You can select [[Image]], [[Music]], [[Video]], [[Game]] in Upload Manager in the main menu:
![[upload_mgr.png]]
- [[Drivers|GPU Driver]] & [[Drivers|Network Driver]] is also available when [[Drivers (Research)]] have been unlocked
- [[Requests]] can be obtained through [[Requests Artifacts]] and provide a singular upload (not auto-repeated)

## File Size
- [[Image]], [[Music]], [[Video]], [[Game]], [[Requests]]
	- It would use your current level to calculate the amount of base file size with many other factor, This is calculated by
	 $\Huge 1\times2^{\huge level-upload\_level}\times\huge\\multi\times\\buffer\times\\compression$ 
	 $level \Rightarrow$ Current [[Level]]
	 $upload\_level\Rightarrow$  $1$ if you have [[Compression(Perk)|Compression Perk]] or else it would be $0$
	 $multi \Rightarrow$ File size multiplier of the file
	 $buffer\Rightarrow$ Random value between $0.8$ and $1.2$
	 $compression \Rightarrow$ [[Compression]] value through upgrade from [[Compression(Talent)]] and [[Modules]] attribute
	 - [[Image]] have File size multiplier of $1$
	 - [[Music]] have File size multiplier of $2$
	 - [[Video]] have File size multiplier of $4$
	 - [[Game]] have File size multiplier of $8$
	 - [[Requests]] have File size multiplier of $1024$
- [[Drivers]]
	- The file size is purely determined by the [[Drivers]] version
	 $\huge1e16\times2^{version}$ 
	 $version \Rightarrow$ the version of THE [[Drivers|GPU Driver]] or [[Drivers|Network Driver]] for each
	 The version can be obtained literally, For example:
	 $\Large 36.2.5 \Rightarrow3625$ 
	 However, you have to kind in mind that on upload page, it display the next version so you should always minus 1 when you are checking for upload panel