import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import Delete


def delete_revisions():
  """

  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """
  creds, _ = google.auth.default()

  try:
    # create drive api client
    service = build("drive", "v3", credentials=creds)

    Delete https://www.googleapis.com/drive/v2/files/{fileId}/revisions/{revisionId} 

  except HttpError as error:
    print(f"An error occurred: {error}")
    file = None

  return file.get("id")


if __name__ == "__main__":
  delete_revisions()