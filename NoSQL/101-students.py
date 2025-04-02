#!/usr/bin/env python3
""" Top students """


def top_students(mongo_collection):
    """
    Returns all students sorted by average score

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of students sorted by average score (descending)
    """
    return mongo_collection.aggregate([
        {
            # Calculate the average score for each student
            "$project": {
                "name": "$name",
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            # Sort by averageScore in descending order
            "$sort": {
                "averageScore": -1
            }
        }
    ])
