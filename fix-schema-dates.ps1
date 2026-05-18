# Fix datePublished / dateModified across six service pages
$enc = [System.Text.UTF8Encoding]::new($false)
$base = 'C:\Users\Инна\Desktop\projects\lumo-ai-agency\services'

# ------------------------------------------------------------------
# 1. ai-automations.html — already has datePublished 2026-03-08,
#    just add dateModified after it
# ------------------------------------------------------------------
$path = "$base\ai-automations.html"
$content = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)
$search = '"datePublished": "2026-03-08",'
if ($content.Contains($search) -and (-not $content.Contains('"dateModified"'))) {
    $replace = $search + [Environment]::NewLine + '        "dateModified": "2026-05-13",'
    $content = $content.Replace($search, $replace)
    [System.IO.File]::WriteAllText($path, $content, $enc)
    Write-Host "ai-automations.html: dateModified added"
} else {
    Write-Host "ai-automations.html: no change needed"
}

# ------------------------------------------------------------------
# Helper: for pages with no datePublished, insert both fields
# after the service url line
# ------------------------------------------------------------------
function Add-Dates {
    param($file, $urlSlug)
    $p = "$base\$file"
    $c = [System.IO.File]::ReadAllText($p, [System.Text.Encoding]::UTF8)
    $s = '"url": "https://lumoaiagency.com/services/' + $urlSlug + '",'
    if ($c.Contains($s) -and (-not $c.Contains('"datePublished"'))) {
        $r = $s + [Environment]::NewLine + '        "datePublished": "2026-03-01",' + [Environment]::NewLine + '        "dateModified": "2026-05-13",'
        $c = $c.Replace($s, $r)
        [System.IO.File]::WriteAllText($p, $c, $enc)
        Write-Host "$file : datePublished + dateModified added"
    } else {
        Write-Host "$file : no change needed"
    }
}

Add-Dates "google-ads.html"   "google-ads"
Add-Dates "meta-ads.html"     "meta-ads"
Add-Dates "ai-development.html" "ai-development"
Add-Dates "voice-ai.html"     "voice-ai"
Add-Dates "ai-outbound.html"  "ai-outbound"

Write-Host "Done."
