# ============================================================
# Defining your own testing here
# ============================================================

import securefileuploaderapi
import NLPanalysisapi
import newsingesterapi

def test_securefileuploader():
  assert SecureFileUploader().get() == "Hello world"
