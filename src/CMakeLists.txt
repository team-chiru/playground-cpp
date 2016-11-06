
############################################################
#### GET PROJECT SOURCES
############################################################
file ( GLOB_RECURSE SOURCE_FILES ./* )
set (SOURCE_FILES ${SOURCE_FILES} PARENT_SCOPE )
