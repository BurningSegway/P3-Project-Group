#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "ur_client_library::urcl" for configuration "RelWithDebInfo"
set_property(TARGET ur_client_library::urcl APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(ur_client_library::urcl PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/liburcl.so"
  IMPORTED_SONAME_RELWITHDEBINFO "liburcl.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS ur_client_library::urcl )
list(APPEND _IMPORT_CHECK_FILES_FOR_ur_client_library::urcl "${_IMPORT_PREFIX}/lib/liburcl.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
