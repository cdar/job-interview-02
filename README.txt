To initialize environment for local development run:
    $ bash create_env.sh

To create default users (admin:admin, user0:user0 ... user2:user2)
    $ source venv/bin/activate
    $ python create_users.py

To run server:
    $ bash start_server.sh

To run api client:
    $ source venv/bin/activate
    $ pip install -r requirements-api-client.txt
    $ python api_client.py

Consider:
    - bootstrap form validation
        https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html#rendering-bootstrap-4-forms
    - internationalization

Postgresql error:
2019-05-29T00:02:20.039122+00:00 app[web.1]: [heroku-exec] Starting
2019-05-29T00:02:21.042865+00:00 app[web.1]: [2019-05-29 00:02:21 +0000] [4] [INFO] Starting gunicorn 19.9.0
2019-05-29T00:02:21.043850+00:00 app[web.1]: [2019-05-29 00:02:21 +0000] [4] [INFO] Listening at: http://0.0.0.0:30761 (4)
2019-05-29T00:02:21.044090+00:00 app[web.1]: [2019-05-29 00:02:21 +0000] [4] [INFO] Using worker: sync
2019-05-29T00:02:21.049745+00:00 app[web.1]: [2019-05-29 00:02:21 +0000] [47] [INFO] Booting worker with pid: 47
2019-05-29T00:02:21.191672+00:00 app[web.1]: [2019-05-29 00:02:21 +0000] [51] [INFO] Booting worker with pid: 51
2019-05-29T00:02:21.308302+00:00 heroku[web.1]: State changed from starting to up
2019-05-29T00:02:18.000000+00:00 app[api]: Build succeeded
2019-05-29T00:02:41.115126+00:00 heroku[router]: at=info method=GET path="/" host=shrouded-badlands-60193.herokuapp.com request_id=3b4b8daf-857d-4c23-8eba-51b89cc4ae8e fwd="89.76.108.132" dyno=web.1 connect=1ms service=11279ms status=500 bytes=156698 protocol=https
2019-05-29T00:02:41.106136+00:00 app[web.1]: Internal Server Error: /
2019-05-29T00:02:41.106148+00:00 app[web.1]: Traceback (most recent call last):
2019-05-29T00:02:41.106151+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/contrib/sessions/backends/base.py", line 189, in _get_session
2019-05-29T00:02:41.106153+00:00 app[web.1]: return self._session_cache
2019-05-29T00:02:41.106155+00:00 app[web.1]: AttributeError: 'SessionStore' object has no attribute '_session_cache'
2019-05-29T00:02:41.106157+00:00 app[web.1]:
2019-05-29T00:02:41.106159+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2019-05-29T00:02:41.106160+00:00 app[web.1]:
2019-05-29T00:02:41.106162+00:00 app[web.1]: Traceback (most recent call last):
2019-05-29T00:02:41.106164+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/db/backends/utils.py", line 84, in _execute
2019-05-29T00:02:41.106166+00:00 app[web.1]: return self.cursor.execute(sql, params)
2019-05-29T00:02:41.106168+00:00 app[web.1]: psycopg2.errors.UndefinedTable: relation "django_session" does not exist
2019-05-29T00:02:41.106169+00:00 app[web.1]: LINE 1: ...ession_data", "django_session"."expire_date" FROM "django_se...
2019-05-29T00:02:41.106171+00:00 app[web.1]: ^
2019-05-29T00:02:41.106173+00:00 app[web.1]:
2019-05-29T00:02:41.106174+00:00 app[web.1]:
2019-05-29T00:02:41.106176+00:00 app[web.1]: The above exception was the direct cause of the following exception:
2019-05-29T00:02:41.106177+00:00 app[web.1]:
2019-05-29T00:02:41.106179+00:00 app[web.1]: Traceback (most recent call last):
2019-05-29T00:02:41.106181+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/core/handlers/exception.py", line 34, in inner
2019-05-29T00:02:41.106182+00:00 app[web.1]: response = get_response(request)
2019-05-29T00:02:41.106184+00:00 app[web.1]: File "/app/secureaccesssite/secureaccess/middleware.py", line 11, in __call__
2019-05-29T00:02:41.106186+00:00 app[web.1]: if request.user.is_authenticated:
2019-05-29T00:02:41.106187+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/utils/functional.py", line 256, in inner
2019-05-29T00:02:41.106189+00:00 app[web.1]: self._setup()
2019-05-29T00:02:41.106191+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/utils/functional.py", line 392, in _setup
2019-05-29T00:02:41.106192+00:00 app[web.1]: self._wrapped = self._setupfunc()
2019-05-29T00:02:41.106194+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/contrib/auth/middleware.py", line 24, in <lambda>
2019-05-29T00:02:41.106196+00:00 app[web.1]: request.user = SimpleLazyObject(lambda: get_user(request))
2019-05-29T00:02:41.106197+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/contrib/auth/middleware.py", line 12, in get_user
2019-05-29T00:02:41.106199+00:00 app[web.1]: request._cached_user = auth.get_user(request)
2019-05-29T00:02:41.106201+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/contrib/auth/__init__.py", line 182, in get_user
2019-05-29T00:02:41.106202+00:00 app[web.1]: user_id = _get_user_session_key(request)
2019-05-29T00:02:41.106204+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/contrib/auth/__init__.py", line 59, in _get_user_session_key
2019-05-29T00:02:41.106206+00:00 app[web.1]: return get_user_model()._meta.pk.to_python(request.session[SESSION_KEY])
2019-05-29T00:02:41.106207+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/contrib/sessions/backends/base.py", line 54, in __getitem__
2019-05-29T00:02:41.106210+00:00 app[web.1]: return self._session[key]
2019-05-29T00:02:41.106211+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/contrib/sessions/backends/base.py", line 194, in _get_session
2019-05-29T00:02:41.106213+00:00 app[web.1]: self._session_cache = self.load()
2019-05-29T00:02:41.106215+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/contrib/sessions/backends/db.py", line 43, in load
2019-05-29T00:02:41.106216+00:00 app[web.1]: s = self._get_session_from_db()
2019-05-29T00:02:41.106218+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/contrib/sessions/backends/db.py", line 34, in _get_session_from_db
2019-05-29T00:02:41.106220+00:00 app[web.1]: expire_date__gt=timezone.now()
2019-05-29T00:02:41.106222+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/db/models/manager.py", line 82, in manager_method
2019-05-29T00:02:41.106223+00:00 app[web.1]: return getattr(self.get_queryset(), name)(*args, **kwargs)
2019-05-29T00:02:41.106225+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/db/models/query.py", line 402, in get
2019-05-29T00:02:41.106227+00:00 app[web.1]: num = len(clone)
2019-05-29T00:02:41.106228+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/db/models/query.py", line 256, in __len__
2019-05-29T00:02:41.106230+00:00 app[web.1]: self._fetch_all()
2019-05-29T00:02:41.106231+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/db/models/query.py", line 1242, in _fetch_all
2019-05-29T00:02:41.106233+00:00 app[web.1]: self._result_cache = list(self._iterable_class(self))
2019-05-29T00:02:41.106235+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/db/models/query.py", line 55, in __iter__
2019-05-29T00:02:41.106236+00:00 app[web.1]: results = compiler.execute_sql(chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size)
2019-05-29T00:02:41.106238+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 1100, in execute_sql
2019-05-29T00:02:41.106240+00:00 app[web.1]: cursor.execute(sql, params)
2019-05-29T00:02:41.106241+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/db/backends/utils.py", line 99, in execute
2019-05-29T00:02:41.106243+00:00 app[web.1]: return super().execute(sql, params)
2019-05-29T00:02:41.106245+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/db/backends/utils.py", line 67, in execute
2019-05-29T00:02:41.106247+00:00 app[web.1]: return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
2019-05-29T00:02:41.106254+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/db/backends/utils.py", line 76, in _execute_with_wrappers
2019-05-29T00:02:41.106256+00:00 app[web.1]: return executor(sql, params, many, context)
2019-05-29T00:02:41.106258+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/db/backends/utils.py", line 84, in _execute
2019-05-29T00:02:41.106260+00:00 app[web.1]: return self.cursor.execute(sql, params)
2019-05-29T00:02:41.106261+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/db/utils.py", line 89, in __exit__
2019-05-29T00:02:41.106263+00:00 app[web.1]: raise dj_exc_value.with_traceback(traceback) from exc_value
2019-05-29T00:02:41.106264+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/django/db/backends/utils.py", line 84, in _execute
2019-05-29T00:02:41.106266+00:00 app[web.1]: return self.cursor.execute(sql, params)
2019-05-29T00:02:41.106268+00:00 app[web.1]: django.db.utils.ProgrammingError: relation "django_session" does not exist
2019-05-29T00:02:41.106270+00:00 app[web.1]: LINE 1: ...ession_data", "django_session"."expire_date" FROM "django_se...
2019-05-29T00:02:41.106272+00:00 app[web.1]: ^
2019-05-29T00:02:41.106344+00:00 app[web.1]:
2019-05-29T00:02:41.107919+00:00 app[web.1]: 10.65.62.237 - - [29/May/2019:00:02:41 +0000] "GET / HTTP/1.1" 500 156487 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0"