from drf_spectacular.utils import extend_schema

list_schema = extend_schema(
    summary="Get list of users",
    responses={
        200: {
            "description": "Successful operation",
            "content": {
                "application/json": {
                    "example": {
                        "users": [
                            {
                                "id": 1,
                                "email": "user1@example.com",
                                "first_name": "John",
                                "last_name": "Doe",
                                "username": "johndoe"
                            },
                            {
                                "id": 2,
                                "email": "user2@example.com",
                                "first_name": "Jane",
                                "last_name": "Smith",
                                "username": "janesmith"
                            }
                        ]
                    }
                }
            }
        },
        401: {
            "description": "Unauthorized",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Unauthorized"
                    }
                }
            },
            "traceback": True
        },
        403: {
            "description": "Forbidden",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Forbidden"
                    }
                }
            },
            "traceback": True
        },
    },
)

create_schema = extend_schema(
    summary="Create a new user",
    responses={
        201: {
            "description": "User created successfully",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "email": "user1@example.com",
                        "first_name": "John",
                        "last_name": "Doe",
                        "username": "johndoe"
                    }
                }
            }
        },
        400: {
            "description": "Bad request",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Bad request"
                    }
                }
            },
            "traceback": True
        },
    },
)

retrieve_schema = extend_schema(
    summary="Get user details",
    responses={
        200: {
            "description": "Successful operation",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "email": "user1@example.com",
                        "first_name": "John",
                        "last_name": "Doe",
                        "username": "johndoe"
                    }
                }
            }
        },
        401: {
            "description": "Unauthorized",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Unauthorized"
                    }
                }
            },
            "traceback": True
        },
        403: {
            "description": "Forbidden",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Forbidden"
                    }
                }
            },
            "traceback": True
        },
        404: {
            "description": "User not found",
            "content": {
                "application/json": {
                    "example": {
                        "error": "User not found"
                    }
                }
            },
            "traceback": True
        },
    },
)

update_schema = extend_schema(
    summary="Update user details",
    responses={
        200: {
            "description": "User updated successfully",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "email": "user1@example.com",
                        "first_name": "John",
                        "last_name": "Doe",
                        "username": "johndoe"
                    }
                }
            }
        },
        400: {
            "description": "Bad request",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Bad request"
                    }
                }
            },
            "traceback": True
        },
        401: {
            "description": "Unauthorized",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Unauthorized"
                    }
                }
            },
            "traceback": True
        },
        403: {
            "description": "Forbidden",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Forbidden"
                    }
                }
            },
            "traceback": True
        },
        404: {
            "description": "User not found",
            "content": {
                "application/json": {
                    "example": {
                        "error": "User not found"
                    }
                }
            },
            "traceback": True
        },
    },
)

partial_update_schema = extend_schema(
    summary="Partially update user details",
    responses={
        200: {
            "description": "User updated successfully",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "email": "user1@example.com",
                        "first_name": "John",
                        "last_name": "Doe",
                        "username": "johndoe"
                    }
                }
            }
        },
        400: {
            "description": "Bad request",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Bad request"
                    }
                }
            },
            "traceback": True
        },
        401: {
            "description": "Unauthorized",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Unauthorized"
                    }
                }
            },
            "traceback": True
        },
        403: {
            "description": "Forbidden",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Forbidden"
                    }
                }
            },
            "traceback": True
        },
        404: {
            "description": "User not found",
            "content": {
                "application/json": {
                    "example": {
                        "error": "User not found"
                    }
                }
            },
            "traceback": True
        },
    },
)

destroy_schema = extend_schema(
    summary="Delete user",
    responses={
        204: {"description": "User deleted successfully"},
        401: {
            "description": "Unauthorized",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Unauthorized"
                    }
                }
            },
            "traceback": True
        },
        403: {
            "description": "Forbidden",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Forbidden"
                    }
                }
            },
            "traceback": True
        },
        404: {
            "description": "User not found",
            "content": {
                "application/json": {
                    "example": {
                        "error": "User not found"
                    }
                }
            },
            "traceback": True
        },
    },
)
