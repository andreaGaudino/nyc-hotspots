from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllProviders():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select a.* , sum(t.Milliseconds) as totD
                        from album a , track t 
                        where a.AlbumId = t.AlbumId 
                        group by a.AlbumId 
                        having totD > %s """
        cursor.execute(query, (d,))

        for row in cursor:
            result.append(Album(**row))
        cursor.close()
        conn.close()
        return result
