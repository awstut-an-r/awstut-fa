FROM public.ecr.aws/lambda/python:3.8

COPY index.py ${LAMBDA_TASK_ROOT}
COPY mymodule.py ${LAMBDA_TASK_ROOT}

CMD [ "index.lambda_handler" ]